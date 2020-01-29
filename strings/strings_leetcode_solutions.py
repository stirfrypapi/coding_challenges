import re

class Solution(object):
    def sanitize_string(self, s):
        s = re.sub(r'[^\w\s]', '', s) # remove punctuation
        s = re.sub(r"\s+", '', s) # remove whitespace
        s = s.lower()
        return s

    ###########################################################################
    ###########################################################################
    #### VALID PALINDROME 125 #################################################
    ###########################################################################
    ###########################################################################
    def isPalindrome(self, s):
        """Returns whether s is a valid palindrome."""
        s = self.sanitize_string(s)
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    ###########################################################################
    ###########################################################################
    #### VALID PARENTHESES 20 #################################################
    ###########################################################################
    ###########################################################################
    def isValid(self, s):
        """Returns whether s has valid parentheses."""
        stack = []
        input = s

        opens = {'[', '(', '{'}  # all open parenthesis
        closes = {']', ')', '}'}  # all closing parenthesis

        # trading memory for faster lookup
        matchings = {'[': ']',
                     '(': ')',
                     '{': '}'}

        for bracket in input:
            if bracket in opens:
                # keep track of opening brackets
                stack.append(bracket)
            if bracket in closes:
                if len(stack) == 0:
                    # return false if we get to a closing parenthesis
                    # and there aren't any open parenthesis
                    return False
                # the top of the stack must be the opening for the current
                # closing bracket
                last_open = stack.pop(-1)
                if matchings[last_open] != bracket:
                    return False

        # return true only if the stack is empty and there are no more parenthesis
        # to look at in the input
        return len(stack) == 0

    ###########################################################################
    ###########################################################################
    #### VALID ANAGRAM 242 ####################################################
    ###########################################################################
    ###########################################################################
    def isAnagram(self, s, t):
        """Returns whether s is an anagram of t."""
        s, t = list(self.sanitize_string(s)), list(self.sanitize_string(t))
        s.sort()
        t.sort()
        return s == t

    ###########################################################################
    ###########################################################################
    #### GROUP ANAGRAMS 49 ####################################################
    ###########################################################################
    ###########################################################################
    def groupAnagrams(self, strs):
        """Group strings with same anagrams."""
        d = {}

        for s in strs:
            sanitize = list(self.sanitize_string(s))
            sanitize.sort()
            sanitize = "".join(sanitize)
            if sanitize not in d:
                d[sanitize] = [s]
            else:
                d[sanitize].append(s)

        res = []
        for key, value in d.items():
            res.append(value)
        return res

    ###########################################################################
    ###########################################################################
    #### LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS 3 #####################
    ###########################################################################
    ###########################################################################
    def lengthOfLongestSubstring(self, s):
        """Return length of longest substring with no repeating characters."""
        chars_dict, start, max_len = {}, 0, 0

        for i in range(len(s)):
            if s[i] in chars_dict and start <= chars_dict[s[i]]:
                start = chars_dict[s[i]] + 1
            else:
                max_len = max(max_len, i - start + 1)

            chars_dict[s[i]] = i

        return max_len

if __name__ == "__main__":
    s = Solution()
    ###########################################################################
    ###########################################################################
    #### VALID PALINDROME 125 #################################################
    ###########################################################################
    ###########################################################################
    print("Valid Palindrome 125")
    print(s.isPalindrome("racecar")) # True
    print(s.isPalindrome("A man, a plan, a canal: Panama")) # True
    print(s.isPalindrome("race a car"))  # False

    ###########################################################################
    ###########################################################################
    #### VALID PARENTHESES 20 #################################################
    ###########################################################################
    ###########################################################################
    print('Valid Parentheses 20')
    print(s.isValid("()[]{}")) # True
    print(s.isValid("(}"))  # False
    print(s.isValid("([)]"))  # False

    ###########################################################################
    ###########################################################################
    #### VALID ANAGRAM 242 ####################################################
    ###########################################################################
    ###########################################################################
    print("Valid Anagram 242")
    print(s.isAnagram("anagram", "naamarg")) # True

    ###########################################################################
    ###########################################################################
    #### GROUP ANAGRAMS 49 ####################################################
    ###########################################################################
    ###########################################################################
    print("Group Anagrams 49")
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

    ###########################################################################
    ###########################################################################
    #### LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS 3 #####################
    ###########################################################################
    ###########################################################################
    print("Longest Substring w/o Repeating Characters 3")
    print(s.lengthOfLongestSubstring("pwwkew")) # 3

    ###########################################################################
    ###########################################################################
    #### LONGEST REPEATING CHARACTER REPLACEMENT ##############################
    ###########################################################################
    ###########################################################################
