# https://leetcode.com/problems/find-the-duplicate-number/
# 287. Find the Duplicate Number
# Medium
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and uses only constant extra space

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in nums:
            if nums.count(i) >= 2:
                return i

# 2nd variant(faster):
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        visited = set()
        for num in nums:
            if num in visited:
                return num
            visited.add(num)