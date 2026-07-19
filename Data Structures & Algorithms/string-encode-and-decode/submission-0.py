class Solution:

    def encode(self, strs: List[str]) -> str:
        op = ""
        for s in strs:
            op = op + str(len(s))+"#"+s
        return op

    def decode(self, s: str) -> List[str]:
        i=0
        op = []
        while(i<len(s)):
            j = i
            while(s[j]!= "#"):
                j = j+1
            print(i,j)
            x = int(s[i:j])
            op.append(s[j+1:j+1+x])
            i= j+x +1
            #print(op)
        return op

