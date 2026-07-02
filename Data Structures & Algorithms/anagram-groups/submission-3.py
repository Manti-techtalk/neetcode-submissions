class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            word = tuple(sorted(i))
            if word in d:
                d[word].append(i)
            else:
                d[word] = [i]
        return list(d.values())