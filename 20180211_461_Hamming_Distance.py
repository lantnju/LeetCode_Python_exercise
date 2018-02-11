class Solution(object):        
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # transform x, y to binary expression
        x_binary = bin(x)[2:][::-1]
        y_binary = bin(y)[2:][::-1]
        
        # longthen the shorter one with '0'
        if len(x_binary) < len(y_binary):
            x_binary += (len(y_binary) - len(x_binary)) * '0'
        else:
            y_binary += (len(x_binary) - len(y_binary)) * '0'
        
        # calculate the number
        num = 0
        for i in range(len(x_binary)):
            if x_binary[i] != y_binary[i]:
                num += 1
        # return the result
        return num
