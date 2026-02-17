class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        seen=[]
        for bulb in bulbs:
            if bulb in seen:
                seen.remove(bulb)
            else:
                seen.append(bulb)
        seen.sort()
        return seen
        