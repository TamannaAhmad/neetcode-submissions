class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for i in strs:
            counts = [0] * 26
            for j in i:
                counts[ord(j) - ord('a')] += 1
            groups[tuple(counts)].append(i)
        return list(groups.values())