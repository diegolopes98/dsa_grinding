from problems.is_anagram import isAnagra
from tests.base_test import ParameterizedTestCase


class TestIsAnagram(ParameterizedTestCase):
    function_under_test = isAnagra

    test_cases = [
        ("basic anagram", ("anagram", "nagaram"), True),
        ("not anagram", ("rat", "car"), False),
        ("empty strings", ("", ""), True),
        ("single character same", ("a", "a"), True),
        ("single character different", ("a", "b"), False),
        ("different lengths", ("abc", "ab"), False),
        ("same string", ("hello", "hello"), True),
        ("case sensitive different", ("Listen", "silent"), False),
        ("case sensitive anagram", ("listen", "silent"), True),
        ("with spaces", ("a gentleman", "elegant man"), True),
        ("numbers anagram", ("12321", "32112"), True),
        ("numbers not anagram", ("123", "456"), False),
        ("repeated characters anagram", ("aabbcc", "abcabc"), True),
        ("repeated characters not anagram", ("aabbcc", "aabbc"), False),
        ("long anagram", ("conversation", "voices rant on"), False),
        ("palindrome", ("racecar", "racecar"), True),
        ("reverse", ("abc", "cba"), True),
        ("mixed case and symbols", ("A man a plan a canal Panama", "Amanaplanacanalpanama"), False),
        ("unicode characters", ("café", "éfac"), True),
        ("special characters", ("a!b@c#", "#c@b!a"), True),
    ]


if __name__ == "__main__":
    import unittest

    unittest.main()