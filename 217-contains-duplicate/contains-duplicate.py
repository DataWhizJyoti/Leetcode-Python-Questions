class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """ Brute Force 
            Time Complexity-O(N^2)
            Space Complexity-O(1)
        
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i]==nums[j]:
                    return True
        return False

        Better Solution
        Time Complexity-O(NlogN)
        Space Complexity-O(1)
        
        nums.sort()
        for i in range(0,len(nums)-1):
            if nums[i]==nums[i+1]:
                return True
        return False

        Optimal Solution
        Time Complexity-O(N)
        Space Complexity-O(N)"""

        hashset=set()
        for i in range(0,len(nums)):
            if nums[i] in hashset:
                return True
            else:
                hashset.add(nums[i])
        return False
        