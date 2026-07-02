from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:  # Ensure there are at least two stones to compare
            stones.sort()  # Sort stones so that the largest are at the end
            first = stones.pop()  # Remove the heaviest stone
            second = stones.pop()  # Remove the second heaviest stone
            
            if first != second:  # If they are not equal, push the difference back
                stones.append(abs(first - second))

        return stones[0] if stones else 0  # Return the last remaining stone or 0
