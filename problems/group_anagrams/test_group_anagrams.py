from problems.group_anagrams.solution import group_anagrams
from test_utils.base_in_out_test import BaseInOutTestCase


class TestGroupAnagrams(BaseInOutTestCase):
    function_under_test = group_anagrams

    test_cases = [
        ("basic anagrams", (["eat", "tea", "tan", "ate", "nat", "bat"],), [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]),
        ("empty string", ([""],), [[""]]),
        ("single character", (["a"],), [["a"]]),
        ("no anagrams", (["abc", "def", "ghi"],), [["abc"], ["def"], ["ghi"]]),
        ("all same string", (["aaa", "aaa", "aaa"],), [["aaa", "aaa", "aaa"]]),
        ("empty list", ([],), []),
        ("single letter anagrams", (["a", "b", "a"],), [["a", "a"], ["b"]]),
        ("longer anagrams", (["listen", "silent", "hello", "world"],), [["listen", "silent"], ["hello"], ["world"]]),
        ("mixed length anagrams", (["ab", "ba", "abc", "cab", "bca"],), [["ab", "ba"], ["abc", "cab", "bca"]]),
        ("palindrome anagrams", (["racecar", "carecar", "hello"],), [["racecar", "carecar"], ["hello"]]),
        ("repeated characters", (["aab", "aba", "baa", "xyz"],), [["aab", "aba", "baa"], ["xyz"]]),
        ("all anagrams", (["abc", "bca", "cab"],), [["abc", "bca", "cab"]]),
        ("only lowercase", (["eat", "tea", "ate"],), [["eat", "tea", "ate"]]),
        ("single anagram pair", (["ab", "ba"],), [["ab", "ba"]]),
        ("three char anagrams", (["cat", "tac", "act", "dog", "god", "odg"],), [["cat", "tac", "act"], ["dog", "god", "odg"]]),
        ("duplicate strings", (["abc", "bca", "abc"],), [["abc", "bca", "abc"]]),
        ("long strings", (["abcdef", "fedcba", "hello", "world"],), [["abcdef", "fedcba"], ["hello"], ["world"]]),
        ("all unique", (["a", "b", "c", "d"],), [["a"], ["b"], ["c"], ["d"]]),
        ("anagrams with repeats", (["aabbcc", "abcabc", "cabcab", "xyz"],), [["aabbcc", "abcabc", "cabcab"], ["xyz"]]),
    ]


if __name__ == "__main__":
    import unittest

    unittest.main()