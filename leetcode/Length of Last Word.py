'''
Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
 

Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
'''
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if (len(s) == 1 or len(s) == 0):
            return (len(s))
        count = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " " and count == 0:
                count += 0
            if count != 0 and s[i] == " ":
                return count
            if s[i] != " ":
                count +=1
            if count != 0 and i == 0:
                return count