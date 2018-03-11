class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        n = B.count(A[0])
        m = -1
        for i in range(n):
            m = B.index(A[0], m+1)
            if B[m:]+B[:m] == A:
                return True
                
        return False
