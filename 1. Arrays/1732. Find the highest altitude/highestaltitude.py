class Solution():
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        curAlt = 0
        highest = 0

        for i in gain:
            curAlt+=i
            highest = max(curAlt,highest)

        return highest
        