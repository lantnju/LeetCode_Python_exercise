class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        a = list(nums)
        a.sort()
        a.reverse()
        b = []
        b.extend(["Gold Medal", "Silver Medal", "Bronze Medal"])
        b.extend([str(i) for i in range(4,len(a)+1)])
        dic_sporter = dict(zip(a,b))
        result = [dic_sporter[i] for i in nums]
        return result
