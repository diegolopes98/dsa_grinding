from problems.remove_duplicates.solution import remove_duplicates
from test_utils.base_reference_test import BaseReferenceTestCase


def assert_duplicates_removed(original_input, modified_input):
    nums = modified_input[0]
    original_nums = original_input[0]
    expected_unique = []
    for num in original_nums:
        if not expected_unique or num != expected_unique[-1]:
            expected_unique.append(num)

    expected_length = len(expected_unique)
    test_nums = original_input[0].copy()
    actual_length = remove_duplicates(test_nums)

    assert (
        actual_length == expected_length
    ), f"Expected length {expected_length}, got {actual_length}"

    actual_unique = nums[:actual_length]
    assert (
        actual_unique == expected_unique
    ), f"Expected {expected_unique}, got {actual_unique}"


def assert_single_element(original_input, modified_input):
    nums = modified_input[0]
    original_nums = original_input[0]
    actual_length = remove_duplicates(original_input[0].copy())

    assert (
        actual_length == 1
    ), f"Expected length 1 for single element, got {actual_length}"
    assert nums[0] == original_nums[0], f"Expected {original_nums[0]}, got {nums[0]}"


def assert_no_duplicates(original_input, modified_input):
    nums = modified_input[0]
    original_nums = original_input[0]
    actual_length = remove_duplicates(original_input[0].copy())

    assert actual_length == len(
        original_nums
    ), f"Expected length {len(original_nums)}, got {actual_length}"
    assert (
        nums[:actual_length] == original_nums
    ), f"Expected {original_nums}, got {nums[:actual_length]}"


def assert_all_same(original_input, modified_input):
    nums = modified_input[0]
    original_nums = original_input[0]
    actual_length = remove_duplicates(original_input[0].copy())

    assert (
        actual_length == 1
    ), f"Expected length 1 for all same elements, got {actual_length}"
    assert nums[0] == original_nums[0], f"Expected {original_nums[0]}, got {nums[0]}"


class TestRemoveDuplicates(BaseReferenceTestCase):
    function_under_test = remove_duplicates

    test_cases = [
        ("basic duplicates", ([1, 1, 2],), assert_duplicates_removed),
        (
            "multiple duplicates",
            ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4],),
            assert_duplicates_removed,
        ),
        ("single element", ([1],), assert_single_element),
        ("no duplicates", ([1, 2, 3, 4, 5],), assert_no_duplicates),
        ("all same elements", ([2, 2, 2, 2, 2],), assert_all_same),
        ("two duplicates", ([1, 1],), assert_duplicates_removed),
        ("alternating pattern", ([1, 2, 2, 3, 3, 3, 4],), assert_duplicates_removed),
        ("negative numbers", ([-3, -1, -1, 0, 0, 1, 2],), assert_duplicates_removed),
        ("large duplicates", ([1, 1, 1, 1, 1, 2, 2, 2, 3],), assert_duplicates_removed),
        (
            "consecutive duplicates",
            ([1, 2, 2, 2, 3, 4, 4, 5],),
            assert_duplicates_removed,
        ),
        (
            "mixed duplicates",
            ([0, 1, 1, 2, 3, 3, 4, 4, 4, 5],),
            assert_duplicates_removed,
        ),
    ]


if __name__ == "__main__":
    import unittest

    unittest.main()
