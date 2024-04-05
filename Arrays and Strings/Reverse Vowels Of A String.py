'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.

Link:https://leetcode.com/problems/reverse-vowels-of-a-string/description/
'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s
        s = list(s)

        vowels = ['a','e','i','o','u', 'A','E','I','O','U']

        j = n-1 
        i = 0

        while (i < j):
            if s[i] not in vowels:
                i += 1
                continue
            if s[j] not in vowels:
                j -= 1
                continue

            s[i],s[j] = s[j],s[i]
            i += 1
            j -= 1

        return ''.join(s)
