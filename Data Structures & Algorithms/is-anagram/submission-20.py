class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        for i in range(len(s)):
            if s[i] in t:
                if t.index(s[i]) != -1:
                    t = t[:t.index(s[i])] + t[t.index(s[i])+1:]
        print(t)
        return t == ""
        