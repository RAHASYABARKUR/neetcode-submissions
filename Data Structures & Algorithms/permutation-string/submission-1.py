class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Len = len(s1)
        l = 0

        s1Freq = [0] * 26
        for c in s1:
            s1Freq[ord(c) - ord('a')] += 1

        subStrFreq = [0] * 26
        subStr = s2[0:s1Len]

        for c in subStr:
            subStrFreq[ord(c) - ord('a')] += 1

        for r in range(s1Len, len(s2)):
            if s1Freq == subStrFreq:
                return True

            # add new character
            subStrFreq[ord(s2[r]) - ord('a')] += 1

            # remove old character
            subStrFreq[ord(s2[l]) - ord('a')] -= 1

            l += 1

        return s1Freq == subStrFreq
        