class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        kind = []
        kind.append(candies[0])
        kind = list(set(candies))
        if len(kind) <= 0.5*len(candies):
            result = len(kind)
        else:
            result = int(0.5*len(candies))
        
        return result
