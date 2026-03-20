class Solution:
    def twoSum(self, nums, target):#list of num&target value
        n = len(nums)#how many numbers
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] ==  target:
                    return [i, j]