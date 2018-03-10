class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = list(set(nums))
        a_count = [nums.count(i) for i in a]
        re = [a[i] for i in range(len(a)) if a_count[i] >= (1 + len(nums)//2)]
        return re[0]
