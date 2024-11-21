import json
import os
import time
from circular_dlinked_list import Node, CircularDoublyLinkedList
from art import *

os.system("")  # enables ANSI characters in terminal

def move_cursor(x, y):
    '''
    Moves the cursor to the specified location on the terminal.
    Input:
        - x (int): row number
        - y (int): column number
    Returns: N/A
    '''
    print("\033[{1};{0}H".format(x, y), end='')
    
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


def read_json_file(file_path):
    """
    Read data from a JSON file.

    Parameters:
    file_path (str): The path to the JSON file.

    Returns:
    dict: The data loaded from the JSON file.
    """
    with open(file_path, 'r',encoding='utf-8') as file:
        data = json.load(file)
    return data

def add_node(carousel,data,side=None):
    """
    Add a new node with data to the circular doubly-linked list.

    Parameters:
    data: The data to be stored in the new node.
    """
    carousel.add_node(data,side)

def take_user_input(carousel):
    """
    Take user input for selecting the action.

    Returns:
    str: The user input.
    """
    if carousel.get_size()==0:
        print("Type any of the following commands to perform the action:")
        print(' '*8+"ADD: Add an emoji frame")
        print(' '*8+"Q: Quit the program")
        user_input = input("").upper()
        if user_input in ['ADD', 'Q']:
            return user_input
        else:
            return None
    elif carousel.get_size()==1:
        print("Type any of the following commands to perform the action:")
        print(' '*8+"ADD: Add an emoji frame")
        print(' '*8+"DEL: Delete current emoji frame")
        print(' '*8+"INFO: Retrieve info about the current frame")
        print(' '*8+"Q: Quit the program")
        user_input = input("").upper()
        if user_input in ['ADD', 'Q','INFO','DEL']:
            return user_input
        else:
            return None    
    else:
        print("Type any of the following commands to perform the action:")
        print(' '*8+"L: Move left")
        print(' '*8+"R: Move right")
        print(' '*8+"ADD: Add an emoji frame")
        print(' '*8+"DEL: Delete current emoji frame")
        print(' '*8+"INFO: Retrieve info about the current frame")
        print(' '*8+"Q: Quit the program")
        user_input = input("").upper()
        if user_input in ['ADD', 'Q','INFO','DEL','L','R']:
            return user_input
        else:
            return None 
    
def find_emoji_info(emoji, data):
    """
    Find information about the given emoji from the data.
    
    Parameters:
        emoji: The emoji to search for.
        data (dict): The dictionary containing emoji data.
        
    Returns:
        dict: Information about the emoji.
    """
    for category in data:
        emojis = category.get("emojis", {})
        for name, symbol in emojis.items():
            if emoji == symbol:
                return {"name": name, "class": category["class"], "symbol": emoji}

def find_object_to_add(user_input, emojis_data):
    """
    Find the object to be added to the circular doubly-linked list based on the user input.

    Parameters:
    user_input (str): The user input.
    emojis_data (dict): The dictionary containing emoji data.

    Returns:
    str: The object to be added to the circular doubly-linked list.
    """
    user_input_lower = user_input.lower().strip()
    for emoji_dict in emojis_data:
        for name, emoji in emoji_dict["emojis"].items():
            if user_input_lower == name.lower():
                return emoji   
    return None

# Main logic
def main():
    carousel = CircularDoublyLinkedList()
    end = False
    emojis_data = read_json_file('emojis.json')
    while not end:
        clear_screen()
        if carousel.get_size()==1:
            clear_screen()
            single_display(carousel)
        elif carousel.get_size()>1:
            clear_screen()
            display(carousel)          
        user_input = take_user_input(carousel)
        if user_input == 'ADD':
            try:
                if carousel.get_size()<carousel.max_size :
                    if carousel.get_size()==0:
                        print("What do you want to add?")
                        emoji = input()                
                        data = find_object_to_add(emoji, emojis_data)
                        while not data:
                            print_location(0, 6,"\033[0K")
                            print_location(0, 6,"Invalid emoji name. Please enter a valid emoji name.")
                            time.sleep(1)
                            print_location(0, 6,"\033[0K")
                            move_cursor(0, 6)
                            emoji = input()                                      
                            data = find_object_to_add(emoji, emojis_data)
                        add_node(carousel,data)
                        clear_screen()
                        initial_add()
                        time.sleep(1)
                    else:
                        print("What do you want to add?")
                        emoji = input()
                        data = find_object_to_add(emoji, emojis_data)
                        while not data:
                            print_location(0, 21,"\033[0K")
                            print_location(0, 21,"Invalid emoji name. Please enter a valid emoji name.")
                            time.sleep(1)
                            print_location(0, 21,"\033[0K")
                            move_cursor(0, 21)
                            emoji = input()                                      
                            data = find_object_to_add(emoji, emojis_data)
                        wrong=False
                        while not wrong:
                            print_location(0, 22,"\033[0K")
                            move_cursor(0, 22)
                            side = input("On which side do you want to add the emoji frame? (left/right) : ").lower()
                            if side=='left':
                                if carousel.get_size()==1:
                                    clear_screen()
                                    add_left_initial()
                                    time.sleep(1)
                                    wrong=True
                                else:
                                    clear_screen()
                                    add_left(carousel)
                                    time.sleep(1)
                                    wrong=True
                            elif side=='right':
                                if carousel.get_size()==1:
                                    clear_screen()
                                    add_right_initial()
                                    time.sleep(1)
                                    wrong=True
                                else:
                                    clear_screen()
                                    add_right(carousel)
                                    time.sleep(1)
                                    wrong=True
                            else:
                                print_location(0, 22,"\033[0K")
                                print_location(0, 22, 'Enter a valid side as an input')
                                time.sleep(1)  
                        add_node(carousel,data,side)                      
                else:
                    add_node(carousel,data)
            except Exception as e:
                print(e)
                time.sleep(1)
        elif user_input == 'Q':
            print("Exiting the program.")
            time.sleep(1)
            end = True        
        elif user_input == 'INFO':
            info = find_emoji_info(carousel.get_current(), emojis_data)
            print("Object:",info['name'])
            print("Sym: ",info['symbol'])
            print("Class: ",info['class'])
            time.sleep(1)
            print('')
            input('Click any button to continue')
        elif user_input == 'L':
            clear_screen()
            move_left(carousel)
            time.sleep(1)
            carousel.move_prev()
        elif user_input == 'R':
            clear_screen()
            move_right(carousel)
            time.sleep(1)
            carousel.move_next()
        elif user_input == 'DEL':
            if carousel.get_size()==1:
                carousel.remove_node()
                clear_screen()
                final_delete()
                time.sleep(1)
            else:
                carousel.remove_node()
                clear_screen()
                delete(carousel)
                time.sleep(1)
        else :
            input("Invalid option. Click any button to continue.")

if __name__ == "__main__":
    main()