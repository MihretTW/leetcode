class Solution:
    def convertDateToBinary(self, date: str) -> str:
        y=bin(int(date[:4]))[2:]
        m=bin(int(date[5:7]))[2:]
        d=bin(int(date[8:]))[2:]
        return str(y)+"-"+str(m)+"-"+str(d)

        