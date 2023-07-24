# https://leetcode.com/problems/is-subsequence/

# 392. Is Subsequence
# Easy
# Companies

# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from
# the original string by deleting some (can be none) of the characters
# without disturbing the relative positions of the remaining characters.
# (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        key_string = s
        purpose_string = t
        key_last_positions = []
        last_found_purpose = 0
        for letter in key_string:
            position_in_purpose = purpose_string.find(letter, (last_found_purpose))
            key_last_positions.append(position_in_purpose)
            last_found_purpose = position_in_purpose + 1
            if position_in_purpose > len(purpose_string) or position_in_purpose == -1:
                return False
        if len(key_string) == len(key_last_positions):
            return key_last_positions == sorted(key_last_positions)