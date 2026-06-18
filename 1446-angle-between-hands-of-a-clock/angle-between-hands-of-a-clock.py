class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        HA=30*(hour%12) +0.5*minutes
        MA=minutes*6
        d=abs(HA-MA)
        return min(d, 360-d)
        