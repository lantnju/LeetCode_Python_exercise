class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        r = []
        key1 = 'qwertyuiop'
        key2 = 'asdfghjkl'
        key3 = 'zxcvbnm'
        for i in words:
            w = list(i.lower())
            w = list(set(w))
            flag = 1
            if w[0] in key1:
                for j in w:
                    if j not in key1:
                        flag = 0
                        break
            elif w[0] in key2:
                for j in w:
                    if j not in key2:
                        flag = 0
                        break
            elif w[0] in key3:
                for j in w:
                    if j not in key3:
                        flag = 0
                        break
            else:
                flag = 0
            # end of if
            if flag:
                r.append(i)
        # end of for loop
        
        return r
