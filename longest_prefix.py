'''14. Longest Common Prefix
Easy
Topics
Companies

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

class Solution:
    def longest_common_prefix(self, strs: list[str]) -> str:
        minlen = min(strs, key=len)
        strs.remove(minlen)
        lim = 0
        for word in strs:
            for i in range(len(minlen)):
                if minlen[i] != word[i]:
                    break
                else:
                    lim = i-1
            minlen = minlen[:lim]
            return minlen
                
a = Solution()
print(a.longest_common_prefix(["dog","racecar","car"]))
print(a.longest_common_prefix(["flower","flow","flight"]))