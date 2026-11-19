class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        num_dict= {}
        for i in nums:
            num_dict[i] = num_dict.get(i,0)+1
        
        res_list = [[] for i in range(len(nums)+1)]

        for key,val in num_dict.items():
            res_list[val].append(key)
        
        ans = []
        for i in range(len(nums),0,-1):
            for j in res_list[i]:
                ans.append(j)
                if len(ans)==k:
                    return ans