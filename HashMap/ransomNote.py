"""
Given two strings ransomNote and magazine, 
return true if ransomNote can be constructed by using the letters from magazine
and false otherwise.

Each letter in magazine can only be used once in ransomNote.
"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
      """
      use of HashMap
      -> key: character in ransomNote
      -> value: number of times a character appeared in ransomNote
      
      iterate through ransomNote to fill our the hash map (dictionary)
      iterate through magazine to decrement the count of character in ransomNote if found
      (not really allowed in HashMap concept) iterate through keys in the hashmap (i.e. iterating through ransomNote)
      if the count of character is greater than 0. If it is, then return False. Otherwise, return True. 
      
      Corner case:
      - when ransomNote.length > magazine.length
      """
      if len(ransomNote) > len(magazine):
            return False
        
      visited = {}

      for c in ransomNote:
          if c not in visited:
              visited[c] = 1
          else:
              visited[c] += 1

      for c in magazine:
          if c in visited:
              visited[c] -= 1

      for c in ransomNote:
          if visited[c] > 0:
              return False

      return True
