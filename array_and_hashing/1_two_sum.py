from typing import List

# class Solution:
#     @staticmethod
#     def find_index(nums, target, i):
#         for index, value in enumerate(nums):
#             if value == target and index != i:
#                 return index
    
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         ans = []
#         for i in range(len(nums)):
#             rem = target - nums[i]
#             rem_index = Solution.find_index(nums, rem, i)
#             if rem in nums and rem_index != None :
#                 ans.append(i)
#                 ans.append(rem_index)
#                 return ans

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        ans = []
        for index, num in enumerate(nums):
            print(hashMap)
            rem = target - num
            if rem in hashMap:
                ans.extend([hashMap[rem], index])
            hashMap[num] = index
        return ans
    
s = Solution()
print(s.twoSum([3,2,4], 6))