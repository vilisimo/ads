# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to
# get t.

# All occurrences of a character must be replaced with another character while
# preserving the order of characters. No two characters may map to the same
# character, but a character may map to itself.

# Example 1:
#   Input: s = "egg", t = "add"
#   Output: true

# Example 2:
#   Input: s = "foo", t = "bar"
#   Output: false

# Example 3:
#   Input: s = "paper", t = "title"
#   Output: true

# Constraints:
#   1 <= s.length <= 5 * 10^4
#   t.length == s.length
#   s and t consist of any valid ascii character.


class DictSetSolution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        replacements = {}
        mapped = set()
        for s_let, t_let in zip(s, t):
            if (replacement := replacements.get(s_let)):
                if replacement != t_let:
                    return False
            else:
                if t_let in mapped:
                    return False
                replacements[s_let] = t_let
                mapped.add(t_let)
        return True


class LengthComparisonSolution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))


class ArraySolution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sa, ta = [0 for i in range(128)], [0 for i in range(128)]
        for idx, letters in enumerate(zip(s, t)):
            sl, tl  = letters
            if sa[ord(sl)] != ta[ord(tl)]:
                return False
            sa[ord(sl)] = idx + 1
            ta[ord(tl)] = idx + 1
        return True
