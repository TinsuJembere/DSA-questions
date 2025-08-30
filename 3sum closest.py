class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums) - 1
        nums.sort()
        closest_sum = float('inf')

        for i in range(n):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            l, r = i + 1, n
            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]

                if abs(curr_sum - target) < abs(closest_sum - target):
                    closest_sum = curr_sum
                if curr_sum == target:
                    return curr_sum
                elif curr_sum < target:
                    l += 1
                else:
                    r -= 1
        return closest_sum
