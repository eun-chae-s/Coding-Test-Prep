"""
Leetcode: Group Anagrams

Approach 1. Create sort each string by alphabetical order and use the hashtable to store each string

Approach 2. Create a frequency string (ex. a2b1) as a key of the hash map
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        
        for element in strs:
            pattern = ''.join(sorted(element))
            
            if pattern not in anagrams:
                anagrams[pattern] = [element]
            else:
                anagrams[pattern].append(element)
        
        return anagrams.values()
   
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
          anagrams = {}

          for element in strs:
              pattern = [0] * 26
              for e in element:
                  pattern[ord(e) - 97] += 1

              freqString = ''

              for i in range(26):
                  if pattern[i] > 0:
                      freqString = freqString + chr(i + 97) + str(pattern[i])

              if freqString not in anagrams:
                  anagrams[freqString] = [element]
              else:
                  anagrams[freqString].append(element)

          return anagrams.values()
