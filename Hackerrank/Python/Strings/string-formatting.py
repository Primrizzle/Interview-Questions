"""
Date:   2.6.2025
Author: Ashley Primrose
Title:  String Formatting
Description: 
Given an integer, n , print the following values for each integer i from 1 to n :
Decimal
Octal
Hexadecimal (capitalized)
Binary

The four values must be printed on a single line in the order specified above for each i from 1 to number. Each value should be space-padded to match the width of the binary value of number 
and the values should be separated by a single space.

"""
def print_formatted(number):
    for i in range(1, number + 1): 
        deci_number = str(i)
        octal_number = oct(i)[2:]
        hexa_number = hex(i)[2:].upper()
        binary_number = bin(i)[2:]
        width = len(bin(number)[2:]) # Padding width of binary)
        print(deci_number.rjust(width), octal_number.rjust(width), hexa_number.rjust(width), binary_number.rjust(width))
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
