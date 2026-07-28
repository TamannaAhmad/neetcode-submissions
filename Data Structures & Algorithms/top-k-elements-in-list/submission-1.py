class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elem_counts = {}
        for i in nums:
            elem_counts[i] = nums.count(i)

        counts = [x for x in elem_counts.values()]
        counts = sorted(counts, reverse=True)
        values = counts[:k]
        res = [k for k,v in elem_counts.items() if v in values]
        return res