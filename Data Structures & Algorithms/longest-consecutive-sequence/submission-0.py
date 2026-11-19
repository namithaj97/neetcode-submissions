class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for i in num_set:
            if i-1 not in num_set:
                length = 0
                while i+length in num_set:
                    length+=1
                longest = max(longest,length)
        return longest

 # [2,20,4,10,3,4,5]
#  2-1 ==>1 not in list
#  20-1 ==> 19 not in list
#  4-1 ==>3 in the list
