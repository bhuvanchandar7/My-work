import os
from bqueue import BoundedQueue
from bstack import BoundedStack
from time import sleep

os.system("")  # enables ANSI characters in terminal

def show_flasks(flasks, source_flask, destination_flask):
    '''
    Displays the flasks with chemicals, highlighting source and destination flasks.
    Input:
        - flasks (list): List of BoundedStack objects representing the flasks.
        - source_flask (int): Number of the source flask.
        - destination_flask (int): Number of the destination flask.
    Returns:
        - 7*num_rows (int): length of all the flasks.
    '''    
    ANSI = {
        'AA': '\033[41m',  # Red background
        'BB': '\033[44m',  # Blue background
        'CC': '\033[42m',  # Green background
        'DD': '\033[48;5;202m',  # Orange background
        'EE': '\033[43m',  # Yellow background
        'FF': '\033[45m'}  # Magenta background  
    
    max_capacity = max(flask.capacity for flask in flasks)
    num_rows = (len(flasks) + 3) // 4
    for row in range(num_rows):
        for level in range(max_capacity, 0, -1):
            for i in range(row * 4, min((row + 1) * 4, len(flasks))):
                if level == max_capacity and flasks[i].sealed() and not flasks[i].is_empty():
                    print('+--+ ',end='')
                elif level <= len(flasks[i].items):  
                    print(f"|{ANSI[flasks[i].items[level - 1]]}{flasks[i].items[level - 1]:^2}\033[0m| ", end="")  
                else:
                    print("|  | ", end="")
                if i % 4 != 3:  
                    print("  ", end="")
            print()

        for i in range(row * 4, min((row + 1) * 4, len(flasks))):
            print("+--+   " , end="") 
        print()

        for i in range(row * 4, min((row + 1) * 4, len(flasks))):
            if i == source_flask:
                print(f"\033[31m{i + 1:>3}\033[0m    ", end="")
            elif i == destination_flask:
                print(f"\033[32m{i + 1:>3}\033[0m    ", end="")
            else:
                print(f"{i + 1:>3}    ", end="")
        print("\n")
        
    return 7*num_rows

def print_location(x, y, text):
    '''
    Prints text at the specified location on the terminal.
    Input:
        - x (int): row number
        - y (int): column number
        - text (str): text to print
    Returns: N/A
    '''
    print ("\033[{1};{0}H{2}".format(x, y, text))

def clear_screen():
    '''
    Clears the terminal screen for future contents.
    Input: N/A
    Returns: N/A
    '''
    if os.name == "nt":  # windows
        os.system("cls")
    else:
        os.system("clear")  # unix (mac, linux, etc.)
        
def display_error(error):
    '''
    Displays an error message as specificed by "error".
    Input:
        - error (str): error message to display
    Returns: N/A
    '''
    print_location(0,5,"\033[0K")
    print_location(0, 5, error)

def move_cursor(x, y):
    '''
    Moves the cursor to the specified location on the terminal.
    Input:
        - x (int): row number
        - y (int): column number
    Returns: N/A
    '''
    print("\033[{1};{0}H".format(x, y), end='')
    
def read_file(filename):
    '''
    Reads game data from a file.
    Input:
        - filename (str): Name of the file to read from
    Returns:
        - num_flask (int): Number of flasks
        - num_chem (int): Number of chemicals
        - chem_list (list): List of chemicals
    '''    
    with open(filename, "r") as file:
        data = file.readline().strip()
        num_flask, num_chem = int(data[0]), int(data[-1])
        chem_list = [line.strip() for line in file.readlines()]
    return num_flask, num_chem, chem_list

def initialize_game(num_flask, chem_list, queue_size=4, stack_size=4):
    '''
    Initializes the game with flasks and chemicals.
    Input:
        - num_flask (int): Number of flasks
        - chem_list (list): List of chemicals
        - queue_size (int): Size of the bounded queue
        - stack_size (int): Size of each bounded stack
    Returns:
        - bq (BoundedQueue): Bounded queue object
        - flasks (list): List of bounded stack objects representing flasks
    '''    
    bq = BoundedQueue(4)
    flasks = [BoundedStack(4) for _ in range(int(num_flask))]
    for items in chem_list:
        if len(items) != 2:
            num_deq = int(items[0])
            flask = int(items[2])
            for x in range(num_deq):
                chemical = bq.dequeue()
                flasks[flask - 1].push(chemical) 
        else:
                    bq.enqueue(items) if bq.size() < 4 else None
    return bq, flasks    
        
def main():    
    num_flask, num_chem, chem_list = read_file("4f 3c.txt")
    bq, flasks = initialize_game(num_flask, chem_list)

    exit = False
    finish = False
    source=None
    destination=None
    while not exit and not finish:
        clear_screen()
        print_location(0,0,"Magical Flask Game")
        print_location(0,3,"Select source flask: ")
        print_location(0,4,"Select destination flask: ")
        move_cursor(0,6)
        pos=show_flasks(flasks,source,destination)
        count = 0
        proper_1 = False
        while not proper_1 and not exit:
            move_cursor(22,3)
            source = input()
            if not source.isdigit():
                if source.lower() == 'exit':
                    exit = True
                else:
                    display_error("Invalid input. Try again.")
                    print_location(0,3,"\033[0K")
                    print_location(0,3,"Select source flask: ")
            else:
                source = int(source) - 1
                if not 0 <= source < num_flask:
                    display_error("Invalid input. Try again.")
                    print_location(0,3,"\033[0K")
                    print_location(0,3,"Select source flask: ")                    
                    
                elif flasks[source].is_empty() or flasks[source].sealed():
                    display_error("Cannot pour from that flask. Try again.")
                    print_location(0,3,"\033[0K")
                    print_location(0,3,"Select source flask: ")                    
                else:
                    proper_1 = True
                    proper_2 = False
                    while not proper_2 and not exit:
                        move_cursor(27,4)
                        destination = input()
                        if not destination.isdigit():
                            if destination.lower() == 'exit':
                                exit = True
                            else:
                                display_error("Invalid input. Try again.")
                                print_location(0,4,"\033[0K")
                                print_location(0,4,"Select destination flask: ")                                
                        else:
                            destination = int(destination) - 1
                            if not 0 <= destination < num_flask:
                                display_error("Invalid input. Try again.")
                                print_location(0,4,"\033[0K")
                                print_location(0,4,"Select destination flask: ")                                
                            elif source == destination:
                                display_error("Cannot pour into the same flask. Try again.")
                                print_location(0,4,"\033[0K")
                                print_location(0,4,"Select destination flask: ")                                
                            elif flasks[destination].is_full() or flasks[destination].sealed():
                                display_error("Cannot pour into that flask. Try again.")
                                print_location(0,4,"\033[0K")
                                print_location(0,4,"Select destination flask: ")                                
                            else:
                                chemical = flasks[source].pop()
                                flasks[destination].push(chemical)
                                proper_2 = True

        for flask in flasks:
            if flask.sealed():
                count += 1
            if count == num_chem:
                finish = True
                
        if finish:
            move_cursor(0,6)
            show_flasks(flasks,source,destination)            
            print_location(0,pos+6,"You win!")
            sleep(5)

        elif exit:
            move_cursor(0,6)
            show_flasks(flasks,source,destination)            
            print_location(0,pos+6,"Exiting game.")
            sleep(5)

if __name__ == "__main__":
    main()
