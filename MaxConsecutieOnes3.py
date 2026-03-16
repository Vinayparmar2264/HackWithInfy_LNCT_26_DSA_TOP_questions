# class Solution:
#     def longestOnes(self, nums: List[int], k: int) -> int:
#         max_cons = 0
#         max_zero = 0
#         i = 0
#         j = 0
#         temp = 0
#         while j<len(nums):
#             if nums[j] == 1:
#                 temp+=1
#                 max_cons  = max(max_cons, temp)
#                 j+=1
#             elif nums[j] == 0 and max_zero<k :
#                 temp+=1
#                 max_cons = max(max_cons,temp)
#                 max_zero += 1
#                 j+=1
#             else:
#                 i = j
#                 temp = 0
#                 max_zero = 0
 
#         return max_cons


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_ones = 0
        zero_count = 0
        left = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
                
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
                
            max_ones = max(max_ones, right-left+1)
            
        return max_ones 
