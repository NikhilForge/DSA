class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count=0
        count=0
        for i in nums:
            if i==1:
                count=count+1
                max_count=max(count,max_count)
            else:
                count=0
        return max_count

      
        