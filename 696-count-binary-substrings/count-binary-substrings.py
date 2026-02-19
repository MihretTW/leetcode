class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        z=0
        o=0
        count=0
        arr=[]
        for ch in s:
            if ch=='0':
                z+=1
                if o!=0 :
                    arr.append(o)
                o=0
            else:
                o+=1
                if z!=0:
                    arr.append(z)
                z=0
        if z>o:
            arr.append(z)
        elif o>z:
            arr.append(o)
        for i in range(len(arr)-1):
            count+=min(arr[i],arr[i+1])
        print(arr)
        return count

        