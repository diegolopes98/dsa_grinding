from problems.concatenation_of_array.solution import get_concatenation
from test_utils.base_in_out_test import BaseInOutTestCase


class TestGetConcatenation(BaseInOutTestCase):
    function_under_test = get_concatenation

    test_cases = [
        ("basic concatenation", ([1, 2, 1],), [1, 2, 1, 1, 2, 1]),
        ("single element", ([1],), [1, 1]),
        ("two elements", ([1, 3],), [1, 3, 1, 3]),
        ("multiple elements", ([1, 2, 3, 4],), [1, 2, 3, 4, 1, 2, 3, 4]),
        ("negative numbers", ([-1, 0, 1],), [-1, 0, 1, -1, 0, 1]),
        ("duplicate elements", ([2, 2, 2],), [2, 2, 2, 2, 2, 2]),
        ("mixed values", ([0, 1, 0, 1],), [0, 1, 0, 1, 0, 1, 0, 1]),
        ("large numbers", ([1000, 999, 1001],), [1000, 999, 1001, 1000, 999, 1001]),
        ("zeros", ([0, 0, 0],), [0, 0, 0, 0, 0, 0]),
        ("alternating pattern", ([1, 0, 1, 0],), [1, 0, 1, 0, 1, 0, 1, 0]),
        ("five elements", ([5, 4, 3, 2, 1],), [5, 4, 3, 2, 1, 5, 4, 3, 2, 1]),
    ]


if __name__ == "__main__":
    import unittest

    unittest.main()