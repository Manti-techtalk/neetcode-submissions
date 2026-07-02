import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        res = []
        heapq.heapify(stones)
        for n in stones:
            heapq.heappush(res,-n)
        while len(res) > 1:
            x = heapq.heappop(res)
            y = heapq.heappop(res)
            y = abs(y)
            x = abs(x)

            if x != y:
                y = y - x
                heapq.heappush(res,y)
        if len(res) == 0:
            return 0
        return int(abs(res[0]))


