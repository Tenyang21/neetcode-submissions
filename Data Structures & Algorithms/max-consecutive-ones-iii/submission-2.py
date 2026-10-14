class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        res = 0
        countz = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                countz += 1
            while countz > k:
                if nums[l] == 0:
                    countz -= 1
                    l += 1
                else:
                    l += 1
            res = max(res, r - l + 1)
        return res

# Window can have at most k zeros, add right, while zeros > k, shrink l if 0 remove, record after loop. 


