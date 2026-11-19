class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # nums = [-1,0,1,2,-1,-4]
                #  i l         r
        res = []
        for i in range(len(nums)):
            if nums[i]==nums[i-1] and i>0:
                continue
            
            l,r = i+1,len(nums)-1

            while l<r:
                target = nums[i]+nums[l]+nums[r]
                if target>0:
                    r-=1
                elif target<0:
                    l+=1
                else:
                    print('joi')
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return res