class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        visited = set()
        vals = []
        for i,s in enumerate(strs):
            if s in visited:
                continue
            group = [s]
            for j,w in enumerate(strs):
                if i!=j and sorted(s) == sorted(w):
                    group.append(w)
                    visited.add(w)
            vals.append(group)
        return vals