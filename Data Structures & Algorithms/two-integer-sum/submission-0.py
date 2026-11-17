class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            x = target-nums[i]
            if x in hashmap.keys():
                return [hashmap[x], i]
            hashmap[nums[i]] = i

    
