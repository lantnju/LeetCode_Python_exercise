class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        m = 0
        for i in range(1,N+1):
            if self.judge(i):
                m = m+1
        
        return m
        
    def judge(self, n):
        a = set([int(i) for i in str(n)])
        b = a - set([2,5,6,9])
        if b.issubset(set([0,1,8])) and len(b) < len(a):
            return True
        else:
            return False
