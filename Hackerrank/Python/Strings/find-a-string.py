"""
Date:   2.2.2025
Author: Ashley Primrose
Title:  Find a String
Description: 
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. 
String traversal will take place from left to right, not from right to left.
NOTE: String letters are case-sensitive.
"""
def count_substring(string, sub_string):
    l = len(string)
    right = 0 
    count = 0
    
    while right != -1:
        right = string.find(sub_string, right)
        if right != -1: 
            count += 1
            right += 1 
                        
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
