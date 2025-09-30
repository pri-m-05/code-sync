from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
            
        map_groups = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            map_groups[key].append(s)

        return list(map_groups.values())