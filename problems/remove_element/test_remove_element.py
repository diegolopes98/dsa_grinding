from problems.remove_element.solution import remove_element
from test_utils.base_reference_test import BaseReferenceTestCase


def assert_element_removed(original_input, modified_input):
    nums = modified_input[0]
    val = original_input[1]
    original_nums = original_input[0]

    expected_nums = [num for num in original_nums if num != val]
    expected_length = len(expected_nums)

    test_nums = original_input[0].copy()
    actual_length = remove_element(test_nums, val)

    assert (
        actual_length == expected_length
    ), f"Expected length {expected_length}, got {actual_length}"

    actual_remaining = nums[:actual_length]
    assert (
        actual_remaining == expected_nums
    ), f"Expected {expected_nums}, got {actual_remaining}"


def assert_no_elements_to_remove(original_input, modified_input):
    nums = modified_input[0]
    val = original_input[1]
    original_nums = original_input[0]

    actual_length = remove_element(original_input[0].copy(), val)

    assert actual_length == len(
        original_nums
    ), f"Expected length {len(original_nums)}, got {actual_length}"
    assert (
        nums[:actual_length] == original_nums
    ), f"Expected {original_nums}, got {nums[:actual_length]}"


def assert_all_elements_removed(original_input, modified_input):
    nums = modified_input[0]
    val = original_input[1]

    actual_length = remove_element(original_input[0].copy(), val)

    assert (
        actual_length == 0
    ), f"Expected length 0 for all elements removed, got {actual_length}"


def assert_single_element_kept(original_input, modified_input):
    nums = modified_input[0]
    val = original_input[1]
    original_nums = original_input[0]

    actual_length = remove_element(original_input[0].copy(), val)

    assert (
        actual_length == 1
    ), f"Expected length 1, got {actual_length}"
    assert nums[0] == original_nums[0], f"Expected {original_nums[0]}, got {nums[0]}"


def assert_empty_array(original_input, modified_input):
    val = original_input[1]

    actual_length = remove_element(original_input[0].copy(), val)

    assert (
        actual_length == 0
    ), f"Expected length 0 for empty array, got {actual_length}"


class TestRemoveElement(BaseReferenceTestCase):
    function_under_test = remove_element

    test_cases = [
        ("basic removal", ([3, 2, 2, 3], 3), assert_element_removed),
        ("no elements to remove", ([0, 1, 2, 2, 3, 0, 4, 2], 5), assert_no_elements_to_remove),
        ("all elements removed", ([2, 2, 2, 2], 2), assert_all_elements_removed),
        ("single element kept", ([1], 2), assert_single_element_kept),
        ("single element removed", ([1], 1), assert_all_elements_removed),
        ("empty array", ([], 1), assert_empty_array),
        ("remove first element", ([1, 2, 3, 4], 1), assert_element_removed),
        ("remove last element", ([1, 2, 3, 4], 4), assert_element_removed),
        ("remove middle elements", ([1, 2, 2, 3], 2), assert_element_removed),
        ("alternating pattern", ([1, 2, 1, 2, 1], 1), assert_element_removed),
        ("negative numbers", ([-1, -2, -1, 0, 1], -1), assert_element_removed),
        ("large array", ([1, 2, 3, 4, 5, 3, 6, 7, 3, 8], 3), assert_element_removed),
        ("consecutive elements", ([1, 1, 1, 2, 3], 1), assert_element_removed),
        ("zero removal", ([0, 1, 0, 2, 0, 3], 0), assert_element_removed),
        ("mixed values", ([4, 5, 4, 6, 4, 7, 8], 4), assert_element_removed),
    ]


if __name__ == "__main__":
    import unittest

    unittest.main()