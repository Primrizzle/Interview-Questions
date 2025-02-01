"""
Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
"""
if __name__ == '__main__':
    # List to store student records
    students = []
    
    # Read inputs and store in a list of tuples (name, score)
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    
    # Sort the list by scores first and then by name 
    students.sort(key=lambda x: (x[1], x[0]))
    
    # Extract unique sorted scores
    unique_scores = sorted(set(score for _, score in students))
    
    # Find the second lowest score
    second_lowest_score = unique_scores[1]
    
    # Get names of students with the second lowest score
    second_lowest_students = [name for name, score in students if score == second_lowest_score]
    
    # Print names in alphabetical order 
    for student in sorted(second_lowest_students): 
        print(student) 
        
