class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        hours.sort(reverse=True)
        count=0
        for i in range(len(hours)):
            if hours[i]>=target:
                count+=1
            else:
                return count
        return count
