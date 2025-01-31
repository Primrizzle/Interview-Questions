""" 
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.
____________________________________________________________________________________________________________________________
Ex. 1: 
Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.

Ex. 2: 
Input: sentence = "leetcode"
Output: false
"""
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
      # Create a set of all alphabet letters 
        alphabet_set = set('abcdefghijklmnopqrstuvwxyz')
        
      # Create a set from the sentence 
        sentence_set = set(sentence)
        
        return sentence_set.issuperset(alphabet_set)
