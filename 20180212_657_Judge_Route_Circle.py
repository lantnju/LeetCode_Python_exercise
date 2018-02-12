class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        flag_vertical = 0      # the movement in the vertical direction
        flag_horizontal = 0    # the movement in the horizontal direction
        for i in moves:
            if i == "U":
                flag_vertical += 1
            elif i == "D":
                flag_vertical -= 1
            elif i == "R":
                flag_horizontal += 1
            elif i == "L":
                flag_horizontal -= 1
            else:
                print("Wrong moves!")
                return
            # end of if
        # end of for loop
        if flag_vertical == 0 and flag_horizontal == 0:
            result = True
        else:
            result = False
        # end of if
        
        # return the result
        return result
