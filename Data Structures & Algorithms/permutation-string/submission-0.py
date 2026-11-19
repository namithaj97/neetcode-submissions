class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1dict = {}

        for i in range(len(s1)):
            s1dict[s1[i]] = s1dict.get(s1[i], 0) + 1

        l = 0
        s2dict = {}

        for r in range(len(s2)):

            s2dict[s2[r]] = s2dict.get(s2[r], 0) + 1

            if r - l + 1 == len(s1):

                if s1dict == s2dict:
                    return True

            elif r - l + 1 > len(s1):

                s2dict[s2[l]] -= 1

                if s2dict[s2[l]] == 0:
                    del s2dict[s2[l]]

                l += 1

                if s1dict == s2dict:
                    return True

        return False
