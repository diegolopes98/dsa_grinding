from problems.two_sum import two_sum
from tests.base_test import ParameterizedTestCase


class TestTwoSum(ParameterizedTestCase):
    function_under_test = two_sum

    test_cases = [
        ("basic case", ([2, 7, 11, 15], 9), [0, 1]),
        ("multiple solutions returns first", ([3, 3, 4, 2], 6), [0, 1]),
        ("negative numbers", ([-1, -2, -3, -4, -5], -8), [2, 4]),
        ("mixed positive negative", ([-3, 4, 3, 90], 0), [0, 2]),
        ("zero target", ([0, 4, 3, 0], 0), [0, 3]),
        ("large numbers", ([1000000, 2000000, 3000000], 3000000), [0, 1]),
        ("no solution", ([1, 2, 3, 4], 10), []),
        ("two elements only", ([5, 5], 10), [0, 1]),
        ("two elements no solution", ([1, 3], 7), []),
        ("duplicate values different indices", ([2, 5, 5, 11], 10), [1, 2]),
    ]


if __name__ == "__main__":
    import unittest
    unittest.main()
