class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False

        s1_hash= [0]*26
        s2_hash= [0]*26
        for i,x in enumerate(s1):
            s1_hash[ord(x)-ord("a")] +=1
            s2_hash[ord(s2[i])-ord("a")] +=1
        print(s1_hash)
        print(s2_hash)
        if(s1_hash==s2_hash):
            return True
        for i in range(len(s1),len(s2),1):
            s2_hash[ord(s2[i])-ord("a")] +=1
            s2_hash[ord(s2[i-len(s1)])-ord("a")] -=1
            print(s1_hash)
            print(s2_hash)
            if(s1_hash==s2_hash):
                return True
        return False

        
        
        
        