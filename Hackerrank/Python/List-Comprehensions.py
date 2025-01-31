""" 
Let's learn about list comprehensions! You are given three integers i, j, and k representing the dimensions of a cuboid along with an integer n. 
Print a list of all possible coordinates given by (i, j, k) on a 3D grid where the sum of i + j + k is not equal to n. Here, 0 <= i <= x; 0 <= j <= y; 0 <= k <= z; 

Print the list in lexicographic increasing order. 
"""
def check_sum(x, y, z, n):
    new_list = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
    print(new_list)

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    check_sum(x, y, z, n)
    
