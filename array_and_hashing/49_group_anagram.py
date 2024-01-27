from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for s in strs:
            a = [0] * 26
            for i in s:
                a[ord(i) - ord('a')] += 1
            a = tuple(a)
            if a in hashMap:
                hashMap[a].append(s)
            else:
                hashMap[a] = [s]

        return list(hashMap.values())

s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))