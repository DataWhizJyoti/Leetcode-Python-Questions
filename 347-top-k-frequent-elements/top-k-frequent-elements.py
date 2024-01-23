class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        """ Brute Force 
            Time complexity-O(nlogn)
            Space Complexity-O(n)"""
        count={}
        
        for n in nums:
            if n in count:
                count[n]+=1
            else:
                count[n]=1
        
        sorted_tuple=sorted(count.items(), key=lambda x:x[1], reverse=True)
        return [sorted_tuple[i][0] for i in range(k)]