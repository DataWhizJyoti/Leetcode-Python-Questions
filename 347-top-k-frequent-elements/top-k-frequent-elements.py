class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        """ Brute Force 
            Time complexity-O(nlogn)
            Space Complexity-O(n)
        count={}
        
        for n in nums:
            if n in count:
                count[n]+=1
            else:
                count[n]=1
        
        sorted_tuple=sorted(count.items(), key=lambda x:x[1], reverse=True)
        return [sorted_tuple[i][0] for i in range(k)]

        Better Solution
        Time Complexity--O(n)
        Space Complexity--O(n)"""
        
        count={}
        freq=[[]for i in range(len(nums)+1)]
        for n in nums:
            count[n]=1+count.get(n,0)
        for n,c in count.items():
            freq[c].append(n)
        res=[]
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res