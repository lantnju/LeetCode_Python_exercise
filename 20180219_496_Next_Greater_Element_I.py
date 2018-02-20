class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for i in findNums:
            n = nums.index(i)
            for j in range(n,len(nums)):
                if nums[j] > int(i):
                    result.append(nums[j])
                    break
                if j == len(nums)-1:
                    result.append(-1)
        return result
