class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res_set = set()
        l=0
        max_val = 0
        for r in range(len(s)):
            while s[r] in res_set:
                res_set.remove(s[l])
                l+=1
            # print("Res_set",res_set)
            res_set.add(s[r])
            max_val = max(max_val,r-l+1)
        return max_val

    


            