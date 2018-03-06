class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_list = list(s)
        s_list.reverse()
        s_list = [ord(i)-ord('A')+1 for i in s_list]
        r = [s_list[i]*26**i for i in range(len(s_list))]
        return sum(r)
