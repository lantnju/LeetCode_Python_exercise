class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        zero = [elem for elem in nums if elem == 0]
        del nums[:len(zero)]
        nums.extend(zero)
