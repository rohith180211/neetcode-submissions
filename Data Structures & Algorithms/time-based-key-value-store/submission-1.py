class TimeMap:

    def __init__(self):
        self.mp=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mp:
            return ""
        arr=self.mp[key]
        res=""
        left=0
        right=len(arr)-1
        while left<=right:
            mid=left+(right-left)//2
            time,val=arr[mid]
            if time<=timestamp:
                res=val
                left=mid+1
            else:
                right=mid-1
        return res
