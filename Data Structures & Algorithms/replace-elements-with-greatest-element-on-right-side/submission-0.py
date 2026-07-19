class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rev = arr[::-1]
        maxele = rev[0]
        for i in range(1,len(rev),1):
            print(rev[i])
            rev[i],maxele = maxele,max(maxele,rev[i])
            # maxele = max(maxele,rev[i])

        # print(rev)
        rev[0]=-1
        # print(rev)
        return rev[::-1]

        