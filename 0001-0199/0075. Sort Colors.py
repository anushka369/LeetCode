class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i = -1
        j = len(nums)
        k = 0
      
        while k < j:
            if nums[k] == 0:
                i += 1
                nums[i], nums[k] = nums[k], nums[i]
                k += 1
              
            elif nums[k] == 2:
                j -= 1
                nums[j], nums[k] = nums[k], nums[j]
              
            else:
                k += 1

# Link to the problem: https://leetcode.com/problems/sort-colors/
