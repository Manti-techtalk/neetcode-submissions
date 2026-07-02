class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        res = []
        seq = []

        for i in range(len(s)):
            if s[i] not in seen:
                seq.append(s[i])
                seen.add(s[i])
            elif s[i] in seen:
                # then we have a duplicate
                res.append(seq)
                duplicate_index = seq.index(s[i])
                seq = seq[duplicate_index+1:] + [s[i]]
                seen = set(seq)
        res.append(seq)
        return max(len(arr) for arr in res)
        