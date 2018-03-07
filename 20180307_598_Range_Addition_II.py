class Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        # method 1
        #import numpy as np
        #M = np.zeros(m * n).reshape(m, n)
        #for i in ops:
        #    M = self.add_1(M, i)
            
        #n = np.max(M)
        #a = [M[i][j] for i in range(np.size(M,0)) for j in range(np.size(M,1))]
        #return a.count(n)
        
        # method 2
        l = [ops[i][0] for i in range(len(ops))]
        l.append(m)
        p = [ops[i][1] for i in range(len(ops))]
        p.append(n)
        r = int(min(l) * min(p))
        return r
        
    #def add_1(self, M, ops):
        #"""
        #:type m: np.array
        #:type ops: List[int]
        #:rtype: np.array
        #"""
        #import numpy as np
        #for i in range(ops[0]):
        #    for j in range(ops[1]):
        #        M[i][j] = M[i][j] + 1
        
        #return M
