# https://leetcode.com/problems/first-unique-character-in-a-string/
# 387. First Unique Character in a String
# Easy

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.


class Solution:
    def firstUniqChar(self, s: str) -> int:
        string = s

        for letter in string:
            if letter not in string[string.find(letter) + 1::]:
                return string.find(letter)

        return -1