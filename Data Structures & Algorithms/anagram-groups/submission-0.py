class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        num_dict = defaultdict(list)
        for i in strs:
            word = ''.join(sorted(i))
            num_dict[word].append(i)
        return list(num_dict.values())