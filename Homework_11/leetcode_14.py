#https://leetcode.com/problems/longest-common-prefix/
# 14. Longest Common Prefix
# Easy
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_word = min(strs, key=len)
        sw = shortest_word
        k = 0
        matches = 0
        while len(sw) != 0:
            sw = shortest_word[:len(shortest_word)-k]
            for word in strs:
                word = word[:len(shortest_word)-k]
                if sw != word:
                    matches = 0
                    continue
                else:
                    matches += 1
            if matches >= len(strs):
                return sw
                break
            k += 1
        return sw