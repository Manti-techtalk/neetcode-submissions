class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {} # signature and its words

        for word in strs:
            sig = ''.join(sorted(word))
            if sig in d:
                d[sig].append(word)
            else:
                d[sig] = [word]
        print(d)

        return [vals for key,vals in d.items()]
        