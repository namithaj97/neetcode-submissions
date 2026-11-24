class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        r = 0
        stack = []
        output = [0]*len(temperatures)

        for r in range(len(temperatures)):
            while stack and temperatures[stack[-1]]< temperatures[r]:
                print(stack[-1],r)
                output[stack[-1]] = r-stack[-1]
                stack.pop()
            stack.append(r)
        return output
