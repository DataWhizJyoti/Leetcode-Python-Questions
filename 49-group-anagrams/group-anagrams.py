class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        """Brute force---using Sorting
            Time Complexity-O(mnlogn)
            Space Complexity--O(n)
            
        strs_dict={}
        for s in strs:
            sorted_s=''.join(sorted(s))
            if sorted_s not in strs_dict:
                strs_dict[sorted_s]=[]
            strs_dict[sorted_s].append(s)
        return list(strs_dict.values())  
        
        Better Solution---using HashMap
            Time complexity-O(m*n)
            Space Complexity--O(n)
            m---number of strings
            n---average length of all strings"""
                       
        res=defaultdict(list)
        for s in strs:
            count=[0]*26
            for c in s:
                count[ord(c)-ord("a")]+=1
            res[tuple(count)].append(s)
        return res.values()       