class Solution:
    def angleClock(self, hour, minutes):
        # hour hand will not be higher than 12
        # hour hand move 30 per hour, 0.5 per minute
        hourDegree = 30*hour + 0.5*minutes
        # minute hand 
        minDegree = minutes/60*360

        angle = abs(hourDegree-minDegree)
        if angle <= 180:
            return angle
        else:
            return 360-angle

test = Solution()
assert(test.angleClock(12,30)==165)
assert(test.angleClock(3,30)==75)
assert(test.angleClock(3,15)==7.5)
assert(test.angleClock(0,30)==165)
assert(test.angleClock(15,30)==75)
assert(test.angleClock(15,15)==7.5)
