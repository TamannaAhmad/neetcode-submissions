class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []

        for a in range(len(nums)):
            if nums[a] > 0:
                break
            if a > 0 and nums[a]==nums[a-1]:
                continue
            l, r = a+1, len(nums)-1
            while l<r:
                sum = nums[a]+nums[l]+nums[r]
                if sum == 0:
                    out.append([nums[a], nums[l], nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif sum > 0:
                    r-=1
                elif sum < 0:
                    l+=1
        return out