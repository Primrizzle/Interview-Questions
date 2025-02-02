"""
Date:   2/2/2025
Author: Ashley Primrose
Title:  sWAP cASE
Description: 
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
"""
def swap_case(s):
    swapped_sentence = ""
    for char in s:
        if char.isupper(): # Check if upper and change to lower
            swapped_sentence += char.lower() 
        elif char.islower(): # Check if lower and change to upper
            swapped_sentence += char.upper()
        else: # If neither keep character (non-letter characters unchanged)
            swapped_sentence += char  
    return swapped_sentence 
    
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

# Side note, Python method .swapcase() would suffice as well:
"""
def swap_case(s):
    swapped_sentence = "" 
    swapped_sentence = s.swapcase() 
    return swapped_sentence 
    
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
  """
