""" 
Date:   1-31-2025
Author: Ashley Primrose
Title:  Finding the Percentage 
Description: 
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
Print the average of the marks array for the student name provided, showing 2 places after the decimal.
"""

if __name__ == '__main__':
    n = int(input()) # Number of students 
    student_marks = {} # Dictionary to store students and their scores 
    
    for _ in range(n):
        name, *line = input().split() # Split input so first part is names from scores 
        scores = list(map(float, line)) # Convert scores into a list of floats 
        student_marks[name] = scores # Store in dictionary 
    
    # Student name to query 
    query_name = input()
    
    # Calculate the average 
    average_marks = sum(student_marks[query_name]) / len(student_marks[query_name])
    
    # Print to 2 decimal places 
    print(f"{average_marks:.2f}")
