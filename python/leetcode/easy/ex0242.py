# Given two strings s and t, return true if t is an anagram of s, and false
# otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a 
# different word or phrase, typically using all the original letters exactly
# once.

 
# Example 1:
#   Input: s = "anagram", t = "nagaram"
#   Output: true

# Example 2:
#   Input: s = "rat", t = "car"
#   Output: false
 
# Constraints:
#   1 <= s.length, t.length <= 5 * 10^4
#   s and t consist of lowercase English letters.

class InitialSolution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        zipped = zip(s, t)
        initialCounts = {}
        candidateCounts = {}
        for (l1, l2) in zipped:
            initialCounts[l1] = initialCounts.get(l1, 0) + 1
            candidateCounts[l2] = candidateCounts.get(l2, 0) + 1
        
        return initialCounts == candidateCounts
        

class ArraySolution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = [0] * 26
        zipped = zip(s, t)
        for sl, tl in zipped:
            counts[ord(sl) - 97] += 1
            counts[ord(tl) - 97] -= 1

        for count in counts:
            if count != 0:
                return False
        return True


class AlternativeArraySolution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = [0] * 26
        for letter in s:
            counts[ord(letter) - 97] += 1

        for letter in t:
            position = ord(letter) - 97
            if counts[position] <= 0:
                return False
            counts[position] -= 1

        return True