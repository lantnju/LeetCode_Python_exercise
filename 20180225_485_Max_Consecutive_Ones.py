class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_string = ''
        for i in nums:
            num_string += str(i)
        
        new_list = num_string.split("0")
        result = 0
        for i in new_list:
            new_num = list(i)
            new_num = [int(elem) for elem in new_num]
            if sum(new_num) > result:
                result = sum(new_num)
        
        return result
