#
# Author: Rohtash Lakra
#
class SubStr:

    def __init__(self, input: str):
        self.input = input

    def longest_substring_with_k_unique_chars(s, k):
        """
        Finds the longest substring with exactly k unique characters.

        Args:
            s (str): The input string.
            k (int): The number of unique characters.

        Returns:
            str: The longest substring, or an empty string if none found.
        """

        if len(s) < k:
            return ""

        left, right = 0, 0
        max_substring = ""
        char_freq = {}

        while right < len(s):
            char_freq[s[right]] = char_freq.get(s[right], 0) + 1

            while len(char_freq) > k:
                char_freq[s[left]] -= 1
                if char_freq[s[left]] == 0:
                    del char_freq[s[left]]
                left += 1

            if right - left + 1 > len(max_substring):
                max_substring = s[left:right + 1]

            right += 1

        return max_substring

    def longest_substr_with_k_unique_chars(string, k):
        k = int(string[0])
        temp_word = word = string[1:k + 1]
        word_end = k
        while word_end < len(string) - 1:
            if len(set(temp_word)) <= k:
                if len(temp_word) > len(word):
                    word = temp_word
                word_end += 1
                temp_word = temp_word + string[word_end]
            else:
                temp_word = temp_word[1:len(temp_word)]
        if len(temp_word) > len(word):
            word = temp_word

        return word
