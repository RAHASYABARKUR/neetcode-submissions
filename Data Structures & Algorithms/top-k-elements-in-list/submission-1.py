class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter ={}
        res = []
        freq = [[] for i in range(len(nums)+1)]
        for num in nums:
            counter[num]  = counter.get(num,0)+1
        
        for i,n in counter.items():
            freq[n].append(i)

        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res
        return counter
        

        