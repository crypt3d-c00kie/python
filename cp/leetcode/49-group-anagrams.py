

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        groups = collections.defaultdict(list)
        for item in strs:
            groups[tuple(sorted(item))].append(item)
        return groups.values()
        
