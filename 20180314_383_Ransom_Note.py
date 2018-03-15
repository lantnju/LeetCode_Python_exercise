class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine = list(magazine)
        for i in ransomNote:
            if i in magazine:
                magazine.remove(i)
            else:
                return False

        return True
