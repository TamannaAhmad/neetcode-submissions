class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_nums = {}
        
        for i, n in enumerate(nums):
            comp = target - n
            if comp in hash_nums and hash_nums[comp] != i:
                return [hash_nums[comp], i]
            else:
                hash_nums[n] = i
        return []