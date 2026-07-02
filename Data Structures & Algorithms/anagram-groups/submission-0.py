class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        used = set()
        vals = []

        for i, s in enumerate(strs):
            if s in used:
                continue
            group = [s]
            used.add(s)
            for j, w in enumerate(strs):
                if i != j and sorted(s) == sorted(w):
                    group.append(w)
                    used.add(w)
            vals.append(group)

        return vals
