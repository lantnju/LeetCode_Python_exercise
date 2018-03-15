class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictionary = {}
        for index, num in enumerate(numbers):
            if target-num in dictionary:
                a = dictionary[target-num]
                b = index + 1
                return [a,b]
            else:
                dictionary[num] = index + 1
