class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        r = 0 # output
        stone_list = list(S)
        for i in range(len(stone_list)):
            if stone_list[i] in J:
                r = r + 1
        # end of for loop
        
        # return output
        return r
