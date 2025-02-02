"""
Date:   2.2.2025
Author: Ashley Primrose
Title:  Lists 
Description: 
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of n followed by i lines of commands where each command will be of the 7 types listed above. 
Iterate through each command in order and perform the corresponding operation on your list.
"""
if __name__ == '__main__':
    N = int(input()) # Read in n lines of commands 
    my_list = [] # Empty list to perform operations on 
    for i in range(N): 
        command = input().split() # Read command split in parts 
        operation = command[0] # Extract operation name 
        
        if operation == "insert": 
            my_list.insert(int(command[1]), int(command[2]))
        elif operation == "print":
            print(my_list)
        elif operation == "remove": 
            my_list.remove(int(command[1]))
        elif operation == "append":
            my_list.append(int(command[1]))
        elif operation == "sort":
            my_list.sort()
        elif operation == "pop":
            my_list.pop() 
        elif operation == "reverse": 
            my_list.reverse()
        else: 
            print("Invalid operation provided.") 
        
        
        
    
    
