from problems.merge_two_sorted_lists.solution import merge_two_sorted_lists, ListNode
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


class TestMergeTwoSortedLists(BaseInOutTestCase):
    @staticmethod
    def function_wrapper(list1_values, list2_values):
        """Wrapper function that takes two lists of values and returns merged result as values"""
        list1 = create_linked_list(list1_values)
        list2 = create_linked_list(list2_values)
        result = merge_two_sorted_lists(list1, list2)
        return linked_list_to_list(result)

    function_under_test = [function_wrapper]

    test_cases = [
        ("both empty", ([], []), []),
        ("first empty", ([], [1, 2, 4]), [1, 2, 4]),
        ("second empty", ([1, 3, 5], []), [1, 3, 5]),
        ("basic merge", ([1, 2, 4], [1, 3, 4]), [1, 1, 2, 3, 4, 4]),
        ("single elements", ([1], [2]), [1, 2]),
        ("single elements reversed", ([2], [1]), [1, 2]),
        ("first shorter", ([1], [2, 3, 4]), [1, 2, 3, 4]),
        ("second shorter", ([1, 2, 3], [4]), [1, 2, 3, 4]),
        ("no overlap left first", ([1, 2, 3], [4, 5, 6]), [1, 2, 3, 4, 5, 6]),
        ("no overlap right first", ([4, 5, 6], [1, 2, 3]), [1, 2, 3, 4, 5, 6]),
        ("identical lists", ([1, 2, 3], [1, 2, 3]), [1, 1, 2, 2, 3, 3]),
        ("alternating merge", ([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6]),
        ("duplicates within lists", ([1, 1, 2], [1, 3, 3]), [1, 1, 1, 2, 3, 3]),
        ("negative numbers", ([-2, 0, 1], [-1, 0, 2]), [-2, -1, 0, 0, 1, 2]),
        ("all same values", ([5, 5, 5], [5, 5]), [5, 5, 5, 5, 5]),
        ("large difference", ([1, 100], [2, 3, 4, 99]), [1, 2, 3, 4, 99, 100]),
        ("mixed positive negative", ([-3, -1, 1], [-2, 0, 2]), [-3, -2, -1, 0, 1, 2]),
        ("long lists equal length", ([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
        ("long lists unequal", ([1, 5, 9, 13], [2, 3, 4, 6, 7, 8, 10, 11, 12]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
        ("zeros", ([0, 0, 0], [0, 0]), [0, 0, 0, 0, 0]),
    ]


if __name__ == "__main__":
    import unittest

    unittest.main()