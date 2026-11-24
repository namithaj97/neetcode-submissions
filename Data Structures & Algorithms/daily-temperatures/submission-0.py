class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        l =0
        r = 0
        stack = []
        output = [0]*len(temperatures)

        while r<len(temperatures):
            while stack and temperatures[stack[-1]]< temperatures[r]:
                print(stack[-1],r)
                output[stack[-1]] = r-stack[-1]
                stack.pop()
            stack.append(r)
            r+=1
        return output
