class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_set = set(s)
        s_count = [s.index(i) for i in s_set if s.count(i)==1]
        s_count.sort()
        if len(s_count) != 0:
            return s_count[0]
        else:
            return -1
