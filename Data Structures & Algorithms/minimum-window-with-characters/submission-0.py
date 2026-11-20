class Solution:
    def minWindow(self, s: str, t: str) -> str:
        map = {}

        for c in t:
            map[c] = map.get(c, 0) + 1

        l = 0
        ans = ""
        smap = {}
        count = 0

        for r in range(len(s)):

            if s[r] in map:
                smap[s[r]] = smap.get(s[r], 0) + 1

                if smap[s[r]] <= map[s[r]]:
                    count += 1

            while count == len(t):

                if ans == "" or r - l + 1 < len(ans):
                    ans = s[l:r+1]

                if s[l] in map:
                    smap[s[l]] -= 1

                    if smap[s[l]] < map[s[l]]:
                        count -= 1

                l += 1

        return ans


