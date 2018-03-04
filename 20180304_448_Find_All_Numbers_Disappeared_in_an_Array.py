class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #result = []
        #for i in range(1,len(nums)+1):
        #    if i not in nums:
        #        result.append(i)
        
        #return result
        
        nums_set = set(nums)
        all_num_set = set(range(1,len(nums)+1))
        return list(all_num_set-nums_set)
