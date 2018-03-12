class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_list = list(s)
        total = 0
        flag = 1
        for i in range(len(s_list)):
            if i !=len(s_list)-1 and self.level(s_list[i+1])>self.level(s_list[i]) and flag==1 and self.value(s_list[i+1])>self.value(s_list[i]):
                flag = -1
            else:
                flag = 1
            total += flag * self.value(s_list[i])
                
        return total
    
    def level(self, t):
        a = ['I','X','C','M','V','L','D']
        b = [0,1,2,3,3,3,3]
        return b[a.index(t)]
    
    def value(self, t):
        a = ['I','X','C','M','V','L','D']
        b = [1,10,100,1000,5,50,500]
        return b[a.index(t)]
