class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[ps,sp] for ps,sp in zip(position,speed)]
        stack = []
        print(cars)
        rev = sorted(cars)[::-1]
        print(rev)
        for p, s in rev:
            print(p,s)
            stack.append((target - p)/s)
            if len(stack) >= 2 and stack[-1] <=stack[-2]:
                stack.pop()
        return len(stack)

        