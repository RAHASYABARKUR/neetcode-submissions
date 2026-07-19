class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        if len(t)==0:
            return True
        i=0
        for x in s:
            if t[i]==x:
                i+=1
            if i==len(t):
                return 0
        #print(i)
        # if i==len(t):
        #     return True
        return len(t)-i
        