""" 
Given an integer array arr, count how many elements x there are, such that x + 1 is also in arr. If there are duplicates in arr, count them separately.

Example 1:
Input: arr = [1,2,3]
Output: 2
Explanation: 1 and 2 are counted cause 2 and 3 are in arr.

Example 2:
Input: arr = [1,1,3,3,5,5,7,7]
Output: 0
Explanation: No numbers are counted, cause there is no 2, 4, 6, or 8 in arr.
"""
class Solution:
    def countElements(self, arr: List[int]) -> int:
        # Create a set from arr to enable fast lookup
        element_set = set(arr)  
        count = 0 
        
        # Iterate through array and count how many elements have their consecutive element in the set 
        for num in arr : 
            if num + 1 in element_set: 
                # Increment the count if num + 1 exists in the set 
                count += 1 
        return count 
