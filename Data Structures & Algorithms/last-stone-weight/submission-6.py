import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxH = []
        #build the maxheap
        for num in stones:
            heapq.heappush(maxH,-num)
        print(maxH)

        # now operate
        while len(maxH) > 1:
            x = heapq.heappop(maxH)
            y = heapq.heappop(maxH)
            x,y = abs(x),abs(y)

            if x != y:
                y = y - x
                heapq.heappush(maxH,y)

        if len(maxH) == 0:
            return 0
        return int(abs(maxH[0]))


        