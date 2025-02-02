"""
Date:   2.2.2025
Author: Ashley Primrose
Title:  String Split and Join
Description: 
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
Function Description:
Complete the split_and_join function in the editor below.
split_and_join has the following parameters:
  string line: a string of space-separated words
  Returns string: the resulting string
"""
def split_and_join(line):
    new_line = line.split(" ") # Convert line to a list of strings
    newly_joined = "-".join(new_line) # Join list of strings with a hyphen
    return newly_joined
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
