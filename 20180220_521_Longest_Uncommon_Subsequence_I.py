class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        flag = 0
        if len(a) == 0 and len(b) == 0:
            result = -1
        elif len(a) == 0 or len(b) == 0:
            result = max(len(a),len(b))
        elif len(a) == len(b):
            for i in range(len(a)):
                if a[i] != b[i]:
                    flag = 1
                    break
            if flag:
                result = len(a)
            else:
                result = -1
        elif len(a) != len(b):
            result = max(len(a),len(b))
         
        return result
