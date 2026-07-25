class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for st in strs:
            res += str(len(st)) + "#" + st
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            length = ""

            # Read the length
            while s[i] != "#":
                length += s[i]
                i += 1

            i += 1  # Skip '#'

            l = int(length)
            res.append(s[i:i + l])
            i += l

        return res