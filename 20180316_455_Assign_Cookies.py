class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        n = 0
        for i in s:
            if len(g) == 0:
                break
            if g[0] > i:
                continue
            else:
                n = n + 1
                g.remove(g[0])
        
        return n
