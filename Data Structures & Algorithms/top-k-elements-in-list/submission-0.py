class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashSet = defaultdict(int)

        for i in range(len(nums)):
            hashSet[nums[i]] += 1
        
        arr = []
        for num, count in hashSet.items():
            arr.append([count, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res