from problems.contains_duplicate.solution import contains_duplicate
from test_utils.base_in_out_test import BaseInOutTestCase


class TestContainsDuplicate(BaseInOutTestCase):
    function_under_test = [contains_duplicate]

    test_cases = [
        ("has duplicates", ([1, 2, 3, 1],), True),
        ("no duplicates", ([1, 2, 3, 4],), False),
        ("empty array", ([],), False),
        ("single element", ([1],), False),
        ("all same elements", ([5, 5, 5],), True),
        ("two elements duplicate", ([2, 2],), True),
        ("two elements no duplicate", ([1, 2],), False),
        ("negative numbers with duplicate", ([-1, -2, -3, -1],), True),
        ("negative numbers no duplicate", ([-1, -2, -3, -4],), False),
        ("mixed positive negative with duplicate", ([1, -1, 2, 1],), True),
        ("mixed positive negative no duplicate", ([1, -1, 2, -2],), False),
        ("zero with duplicate", ([0, 1, 2, 0],), True),
    ]


if __name__ == "__main__":
    import unittest

    unittest.main()
