'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        length = len(strs[0])
        for i in range(len(strs)):
            if len(strs[i]) < length:
                length = len(strs[i])
        word = strs[0][0:length]
        for i in range(length):
            for j in range(1, len(strs)):
                if strs[j][i] != word[i]:
                    return result
            result += word[i]
        return result
                    