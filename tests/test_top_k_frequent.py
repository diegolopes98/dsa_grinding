from problems.top_k_frequent import top_k_frequent
from tests.base_test import ParameterizedTestCase


class TestTopKFrequent(ParameterizedTestCase):
    function_under_test = top_k_frequent

    test_cases = [
        ("basic example", ([1, 1, 1, 2, 2, 3], 2), [1, 2]),
        ("single element", ([1], 1), [1]),
        ("k equals array length", ([1, 2, 3], 3), [1, 2, 3]),
        ("all same frequency", ([1, 2, 3, 4], 2), [1, 2]),
        ("descending frequency", ([1, 1, 1, 2, 2, 3], 3), [1, 2, 3]),
        ("negative numbers", ([-1, -1, -2, -2, -2, 3], 2), [-2, -1]),
        ("mixed positive negative", ([1, -1, 1, -1, 2], 2), [1, -1]),
        ("large numbers", ([100, 200, 100, 300, 200, 100], 2), [100, 200]),
        ("zeros", ([0, 0, 1, 1, 1, 2], 2), [1, 0]),
        ("single k", ([5, 5, 5, 1, 1, 2], 1), [5]),
        ("duplicate values different freq", ([1, 2, 2, 3, 3, 3], 2), [3, 2]),
        ("all unique elements", ([1, 2, 3, 4, 5], 3), [1, 2, 3]),
        ("two elements same freq", ([1, 1, 2, 2], 2), [1, 2]),
        ("large k", ([1, 1, 2, 2, 3, 3, 4], 4), [1, 2, 3, 4]),
        ("repeated pattern", ([1, 2, 1, 2, 1, 2, 3], 2), [1, 2]),
        ("high frequency single", ([7, 7, 7, 7, 7, 1, 2], 1), [7]),
        ("sequential numbers", ([1, 2, 3, 4, 5, 5, 5], 2), [5, 1]),
        ("random order", ([3, 1, 4, 1, 5, 9, 2, 6, 5], 3), [1, 5, 3]),
        ("zero and positive", ([0, 1, 0, 1, 2, 2, 2], 2), [2, 0]),
        ("edge case small k", ([10, 20, 10, 30, 20, 10], 1), [10]),
    ]


if __name__ == "__main__":
    import unittest

    unittest.main()