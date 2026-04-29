class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        left = 0
        my_set = set()

        for right, char in enumerate(s):
            while char in my_set:
                my_set.remove(s[left])
                left += 1

            my_set.add(char)
            current_size = right - left + 1
            max_length = max(max_length, current_size)
        return max_length