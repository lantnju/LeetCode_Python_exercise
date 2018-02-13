class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        for i in range(left,right+1):
            string = str(i)
            flag = 1
            for j in string:
                if j == "0" or i % int(j) != 0:
                    flag = 0 
                # end of if
            # end of for loop
            if flag:
                result.append(i)
            # end of if
        # end of for loop
        
        return result
