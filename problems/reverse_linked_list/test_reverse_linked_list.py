from problems.reverse_linked_list.solution import reverse_list, ListNode
from test_utils.base_in_out_test import BaseInOutTestCase


def create_linked_list(values):
    """Helper function to create a linked list from a list of values"""
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head):
    """Helper function to convert a linked list to a list of values"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


def assert_reversed_linked_list(test_case, original_input, result):
    """Custom assertion function for linked list reversal"""
    input_values = original_input[0]
    expected_values = list(reversed(input_values)) if input_values else None

    if expected_values is None:
        test_case.assertIsNone(result)
    else:
        actual_values = linked_list_to_list(result)
        test_case.assertEqual(actual_values, expected_values)


class TestReverseListCustom(BaseInOutTestCase):
    @staticmethod
    def function_under_test(values):
        """Wrapper function that takes values and returns result as values"""
        head = create_linked_list(values)
        result = reverse_list(head)
        return linked_list_to_list(result)

    test_cases = [
        ("empty list", ([],), []),
        ("single node", ([1],), [1]),
        ("two nodes", ([1, 2],), [2, 1]),
        ("three nodes", ([1, 2, 3],), [3, 2, 1]),
        ("five nodes", ([1, 2, 3, 4, 5],), [5, 4, 3, 2, 1]),
        ("duplicate values", ([1, 1, 2, 2],), [2, 2, 1, 1]),
        ("negative values", ([-1, 0, 1],), [1, 0, -1]),
        ("all same values", ([5, 5, 5, 5],), [5, 5, 5, 5]),
        ("mixed values", ([10, -5, 0, 3, -1],), [-1, 3, 0, -5, 10]),
        ("alternating pattern", ([1, 0, 1, 0, 1],), [1, 0, 1, 0, 1]),
        ("descending order", ([5, 4, 3, 2, 1],), [1, 2, 3, 4, 5]),
        ("large list", (list(range(1, 11)),), list(range(10, 0, -1))),
    ]


if __name__ == "__main__":
    import unittest

    unittest.main()
