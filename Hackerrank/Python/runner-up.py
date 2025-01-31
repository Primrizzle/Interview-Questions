""" 
Date: 1/30/25
Author: Ashley Primrose 
Description: 
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.

Input Format
The first line contains n. The second line contains an array A[] of n integers each separated by a space.
"""
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    sorted_unique_scores = sorted(set(arr))
    
    print(sorted_unique_scores[-2])
    
    
