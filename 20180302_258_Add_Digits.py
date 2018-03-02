class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_list = list(str(num))
        num_list = [int(x) for x in num_list]
        r = sum(num_list)
        if r >= 10:
            r = self.addDigits(r)
            
        return r
    # follow up
    #   if num == 0:
    #       return 0
    #   elif num % 9 == 0:
    #       return 9
    #   else:
    #       return num % 9
