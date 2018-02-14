class Solution(object):  
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # solution 1 效率低
        #max_min = 0
        # 两两配对，每次保留list中的次大值
        #while len(nums) > 0:
        #    nums.remove(max(nums))
        #    max_min += max(nums)
        #    nums.remove(max(nums))
        # end of while
        
        # solution 2 效率高
        nums.sort()
        max_min = sum(nums[::2])
        return max_min
