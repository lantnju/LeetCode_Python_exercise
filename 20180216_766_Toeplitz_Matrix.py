class Solution:    
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        import numpy as np
        diag_list1 = []
        diag_list2 = []
        matrix = np.array(matrix)
        size_1 = np.size(matrix,1)-1
        size_2 = np.size(matrix,0)-1
        flag = True
        for i in range(size_1):
            diag_list1 = list(np.diag(matrix,i))
            for j in range(len(diag_list1)):
                if diag_list1[j] != diag_list1[0]:
                    flag = False
                    break
            if not flag:
                break
        if flag:
            for i in range(size_2):
                diag_list2 = np.diag(matrix,-i)
                for j in range(len(diag_list2)):
                    if diag_list2[j] != diag_list2[0]:
                        flag = False
                        break
                if not flag:
                    break
        return flag
