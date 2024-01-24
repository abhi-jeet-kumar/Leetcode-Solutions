from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        status = False
        hashMap = {}
        for num in nums:
            if num in hashMap:
                hashMap[num] += 1
                if hashMap[num] == 2:
                    return True
            else:
                hashMap[num] = 1
        return status
    
s = Solution()
print(s.containsDuplicate([1,2,4,5]))