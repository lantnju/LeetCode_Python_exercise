class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = s.split(' ')
        for i in range(len(s_list)):
            s_list[i] = s_list[i][::-1]
        # end of for
        s_new = (' ').join(s_list)
        return s_new
