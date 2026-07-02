class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for word in strs:
            cur = ''.join(sorted(word))
            print(cur)
            if cur in d:
                d[cur].append(word)
            else:
                d[cur] = [word]
        return list(d.values())
        