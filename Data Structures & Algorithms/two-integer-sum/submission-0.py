class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        num_set = {}
        for k,v in enumerate(nums):
            diff = target-v
            if diff in num_set:
                return [num_set[diff],k]
            num_set[v] = k
