class Solution:
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        if (area ** 0.5) % 1 == 0:
            return [int(area ** 0.5), int(area ** 0.5)]
        else:
            L = int(area ** 0.5) + 1
            while area % L != 0:
                L = L + 1
            M = area / L
            return [int(L), int(M)]
