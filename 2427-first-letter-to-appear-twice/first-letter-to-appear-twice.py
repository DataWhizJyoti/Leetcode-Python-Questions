class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
        for i in range(0,len(s)-1):
            for j in range(i+1,len(s)):
                if s[i]==s[j]:
                    return s[j]
                """
        """better Solution-Using set
            Time complexity-O(N)
            Space Complexity-O(N)"""
        
        seen=set()
        for c in s:
            if c in seen:
                return c
            seen.add(c) 