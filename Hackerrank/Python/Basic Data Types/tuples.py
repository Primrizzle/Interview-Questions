"""
Date:   2.2.2025
Author: Ashley Primrose
Title:  Tuples
Description: 
Given an integer,n , and n space-separated integers as input, create a tuple, t , of those n integers. Then compute and print the result of hash(t).
Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.
"""
if __name__ == '__main__':
    n = int(input()) # Read in number of integers 
    integer_list = map(int, input().split()) # Read in integers separated by space 
    t = tuple(integer_list) # Convert to a tuple 
    print(hash(t)) # Compute and print 
