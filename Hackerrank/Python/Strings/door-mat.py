""" 
Date:   2.6.2025
Author: Ashley Primrose
Title:  Designer Door Mat
Description: 
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be X. (N is an odd natural number, and M is 3 times N .)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
"""
# Top half, up to N - 2
N, M = map(int, input().split())
for i in range(1, N, 2): 
   print(('.|.'*i).center(M, '-') )

# Middle
print('WELCOME'.center(M, '-'))

# Bottom half, down from N - 2 
for i in range(N-2, -1, -2): 
   print(('.|.'*i).center(M, '-') )
