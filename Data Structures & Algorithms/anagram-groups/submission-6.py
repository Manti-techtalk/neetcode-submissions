class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for word in strs:
            cur_sig = ''.join(sorted(word))
            if cur_sig in d:
                d[cur_sig].append(word)
            else:
                d[cur_sig] = [word]
        return list(d.values())
        