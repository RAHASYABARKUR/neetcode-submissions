class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict()
        freq =[[] for i in range (len(nums)+1)]
        res = []
        print(len(freq),len(freq[0]))
        for i in nums:
            count[i] = count.get(i,0) + 1
        
        for i,n in count.items():
            freq[n].append(i)
        
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res 
        return count
        
        