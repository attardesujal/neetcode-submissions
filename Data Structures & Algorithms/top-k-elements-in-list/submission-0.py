class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lst=set()
        for i in nums:
            count=0
            
            for j in nums:
                if j in lst:
                    pass
                if i==j:
                    count += 1
            if count>=k:
                lst.add(i)
        return list(lst)