class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = {}
        rescount = 0
        l=0
        maxf = 0
        for r in range(len(s)):
            res[s[r]] = res.get(s[r],0)+1
            maxf = max(maxf,res[s[r]])
            while (r-l+1)- maxf >k:
                res[s[l]]-=1
                l+=1

            rescount = max(rescount,(r-l+1))
        return rescount
