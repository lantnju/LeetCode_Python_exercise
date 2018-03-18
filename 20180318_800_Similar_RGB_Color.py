class Solution(object):
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """
        return '#'+self.findsimilar(color[1:3])+self.findsimilar(color[3:5])+self.findsimilar(color[5:])
    
    def findsimilar(self, str_n):
        all_n = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
        b = int(str_n,16)
        c = 255**2
        for i in all_n:
            a = int(i*2,16)
            if (a-b)**2 < c:
                c = (a-b)**2
                t = i
        
        return t*2
