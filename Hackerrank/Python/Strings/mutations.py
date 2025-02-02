"""
Date:   2-2-2025
Author: Ashley Primrose
Title:  Mutations
Description: 
Read a given string, change the character at a given index and then print the modified string.
"""
def mutate_string(string, position, character):
    l = list(string) 
    l[position] = character
    new_string = "".join(l)
    return new_string
    

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
