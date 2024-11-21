from circular_dlinked_list import Node, CircularDoublyLinkedList

def display(dlist) :
    prev=dlist.before()
    current=dlist.get_current()
    after=dlist.after()
     
    display = """
                                 ↓↓
     __________    |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|    __________
               |   |                            |   |          
               |   |                            |   |          
     {}        |   |             {}             |   |        {}
               |   |                            |   |          
     __________|   |                            |   |__________
                   |____________________________|
    
    """.format(prev,current,after)
    print(display)
    
def single_display(dlist):
    current=dlist.get_current()
        
    single_display = """

                                 ↓↓
                   |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|    
                   |                            |          
                   |                            |        
                   |             {}             |       
                   |                            |         
                   |                            |  
                   |____________________________|
    
                                 
    """.format(current)
    print(single_display)

def delete(dlist) :
    prev=dlist.before()
    after=dlist.after()    
    
    delete = """
                                 /\ 
     __________    |‾‾‾‾‾‾‾‾‾‾‾‾/  \‾‾‾‾‾‾‾‾‾‾‾‾|    __________
               |   |           /    \           |   |                   
               |   |          /_    _\          |   |                   
     {}        |   |            |  |            |   |        {}        
               |   |            |  |            |   |                  
     __________|   |            |  |            |   |__________
                   |____________|  |____________|
                                |__|
    """.format(prev,after)
    print(delete)

def final_delete() :
    
    final_delete = """
                                 /\ 
                   |‾‾‾‾‾‾‾‾‾‾‾‾/  \‾‾‾‾‾‾‾‾‾‾‾‾|   
                   |           /    \           |                    
                   |          /_    _\          |           
                   |            |  |            |       
                   |            |  |            |                  
                   |            |  |            |   
                   |____________|  |____________|
                                |__|
                                 
    """
    print(final_delete)

def move_right(dlist) :
    prev=dlist.before()
    after=dlist.after()
    
    move_right = """
                                             |
     __________    |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾| \     __________
               |   |                         |  \   |                   
               | |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾    \  |                   
     {}        | |            Right               | |        {}        
               | |___________________________    /  |                  
     __________|   |                         |  /   |__________
                   |_________________________| /
                                             |/
    """.format(prev,after)
    print(move_right)

def add_right(dlist) :
    prev=dlist.before()
    after=dlist.after()
    
    add_right = """
                                             |
     __________    |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾| \     __________
               |   |                         |  \   |                   
               | |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾    \  |                   
     {}        | |        Adding Right            | |        {}        
               | |___________________________    /  |                  
     __________|   |                         |  /   |__________
                   |_________________________| /
                                             |/
                                 
    """.format(prev,after)
    print(add_right)

def add_right_initial() :
    
    add_right_initial = """
                                             |
                   |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾| \  
                   |                         |  \          
                 |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾    \          
                 |        Adding Right            |    
                 |___________________________    /    
                   |                         |  /  
                   |_________________________| /
                                             |/
                                 
    """
    print(add_right_initial)
    
def move_left(dlist) :
    prev=dlist.before()
    after=dlist.after()
    
    move_left = """
                     /|                      
     __________     / |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|    __________
               |   /  |                         |   |                   
               |  /    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾| |                   
     {}        | |              Left              | |        {}        
               |  \    ___________________________| |                  
     __________|   \  |                         |   |__________
                    \ |_________________________|
                     \|                      
    """.format(prev,after)
    print(move_left)

def add_left (dlist) :
    prev=dlist.before()
    after=dlist.after()
    
    add_left = """
                     /|                      
     __________     / |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|    __________
               |   /  |                         |   |                   
               |  /    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾| |                   
     {}        | |           Adding Left          | |        {}        
               |  \    ___________________________| |                  
     __________|   \  |                         |   |__________
                    \ |_________________________|
                     \|                      
                                 
    """.format(prev,after)
    print(add_left)

def add_left_initial() :
    
    add_left_initial = """
                     /|                      
                    / |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|   
                   /  |                         |          
                  /    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|      
                 |           Adding Left          |       
                  \    ___________________________|             
                   \  |                         |   
                    \ |_________________________|
                     \|                      
                                 
    """
    
    print(add_left_initial)
def initial_add() :
    
    initial_add = """
                                |‾‾|
                   |‾‾‾‾‾‾‾‾‾‾‾‾|  |‾‾‾‾‾‾‾‾‾‾‾‾|   
                   |            |  |            |                   
                   |            |  |            |                    
                   |           _|  |_           |   
                   |          \      /          |                
                   |           \    /           |   
                   |____________\  /____________|
                                 \/
                                
    """
    print(initial_add)