class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        s = bin(num)[2:]
        s_new = str(int(len(s)*'1') - int(s))
        return int(s_new,2)
