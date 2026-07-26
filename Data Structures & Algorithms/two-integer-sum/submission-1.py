class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_nums = {}
        for i in range(len(nums)):
            hash_nums[nums[i]] = i
        for i, n in enumerate(nums):
            comp = target - n
            if comp in hash_nums and hash_nums[comp] != i:
                return [i, hash_nums[comp]]
        else:
            return []