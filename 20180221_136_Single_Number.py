class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            result = nums[0]
        else:
            new = list(set(nums))
            new.sort()
            nums.sort()
            for i in range(len(new)):
                n = nums.index(new[i])
                if n%2 == 1:
                    result = new[i-1]
                    break
        
        return result
