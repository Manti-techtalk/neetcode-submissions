class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for word in strs:
            cur = "".join(sorted(word))
            print(cur)
            # if cur not in d:
            #     d[strs[cur]] = []

            d[cur] = []

        for word in strs:
            cur = "".join(sorted(word))
            if "".join(sorted(word)) in d:
                d[cur].append(word)

        print(d)
        return list(d.values())