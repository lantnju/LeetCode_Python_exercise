class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        from itertools import combinations as cb
        S_list = list(S)
        possible_list = []
        possible_list.append(S.lower())
        letters = []
        for i in range(len(S_list)):
            if not S_list[i].isdigit():
                letters.append(i)
        for i in range(1,1+len(letters)):
            t = list(cb(letters,i))
            for j in t:
                S = S.lower()
                S_list = list(S)
                p = list(j)
                for q in p:
                    S_list[q] = S_list[q].upper()
                possible_list.append(('').join(S_list))
        
        return possible_list
