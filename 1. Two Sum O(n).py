class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen ={}
        for i in range(0,len(nums)):
            remainder = target - nums[i]
            if remainder in seen:
                return [i,seen[remainder]]
            seen[nums[i]] = i
