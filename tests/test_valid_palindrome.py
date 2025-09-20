from problems.valid_palindrome import isPalindrome
from tests.base_in_out_test import BaseInOutTestCase


class TestIsPalindrome(BaseInOutTestCase):
    function_under_test = isPalindrome

    test_cases = [
        ("basic palindrome", ("A man a plan a canal Panama",), True),
        ("not palindrome", ("race a car",), False),
        ("empty string", ("",), True),
        ("single character", ("a",), True),
        ("two same characters", ("aa",), True),
        ("two different characters", ("ab",), False),
        ("simple palindrome", ("racecar",), True),
        ("simple not palindrome", ("hello",), False),
        ("palindrome with spaces", ("Was it a car or a cat I saw",), True),
        ("mixed case palindrome", ("Madam",), True),
        ("palindrome with punctuation", ("A Santa at NASA",), True),
        ("complex palindrome", ("Mr. Owl ate my metal worm",), True),
        ("palindrome with numbers", ("12321",), True),
        ("not palindrome with numbers", ("12345",), False),
        ("palindrome alphanumeric", ("race a car",), False),
        ("palindrome only letters", ("abccba",), True),
        ("palindrome only numbers", ("12344321",), True),
        ("mixed alphanumeric palindrome", ("A1B2b1a",), True),
        ("special characters only", ("!@#$%^&*()",), True),
        ("palindrome with special chars", ("A!b@a",), True),
        ("long palindrome", ("Able was I ere I saw Elba",), True),
        ("case insensitive", ("AbA",), True),
        ("whitespace palindrome", (" ",), True),
        ("tab and space", ("a\t a",), True),
        ("newline palindrome", ("a\na",), True),
    ]


if __name__ == "__main__":
    import unittest

    unittest.main()