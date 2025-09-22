import unittest
from data_structures.doubly_linked_list.doubly_linked_list import DoublyLinkedList


class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.ll = DoublyLinkedList()

    def test_initial_state(self):
        """Test initial empty state"""
        self.assertIsNone(self.ll.head)
        self.assertIsNone(self.ll.tail)
        self.assertEqual(self.ll.size, 0)

    def test_get_empty_list(self):
        """Test get on empty list"""
        self.assertEqual(self.ll.get(0), -1)
        self.assertEqual(self.ll.get(1), -1)
        self.assertEqual(self.ll.get(-1), -1)

    def test_add_at_head_single(self):
        """Test adding single element at head"""
        self.ll.addAtHead(5)
        self.assertEqual(self.ll.size, 1)
        self.assertEqual(self.ll.head.val, 5)
        self.assertEqual(self.ll.tail.val, 5)
        self.assertIs(self.ll.head, self.ll.tail)
        self.assertEqual(self.ll.get(0), 5)

    def test_add_at_head_multiple(self):
        """Test adding multiple elements at head"""
        self.ll.addAtHead(1)
        self.ll.addAtHead(2)
        self.ll.addAtHead(3)
        self.assertEqual(self.ll.size, 3)
        self.assertEqual(self.ll.get(0), 3)  # Last added is first
        self.assertEqual(self.ll.get(1), 2)
        self.assertEqual(self.ll.get(2), 1)

    def test_add_at_tail_single(self):
        """Test adding single element at tail"""
        self.ll.addAtTail(10)
        self.assertEqual(self.ll.size, 1)
        self.assertEqual(self.ll.head.val, 10)
        self.assertEqual(self.ll.tail.val, 10)
        self.assertIs(self.ll.head, self.ll.tail)
        self.assertEqual(self.ll.get(0), 10)

    def test_add_at_tail_multiple(self):
        """Test adding multiple elements at tail"""
        self.ll.addAtTail(1)
        self.ll.addAtTail(2)
        self.ll.addAtTail(3)
        self.assertEqual(self.ll.size, 3)
        self.assertEqual(self.ll.get(0), 1)
        self.assertEqual(self.ll.get(1), 2)
        self.assertEqual(self.ll.get(2), 3)

    def test_mixed_head_tail_operations(self):
        """Test mixing head and tail operations"""
        self.ll.addAtHead(2)
        self.ll.addAtTail(3)
        self.ll.addAtHead(1)
        self.ll.addAtTail(4)
        # Should be [1, 2, 3, 4]
        self.assertEqual(self.ll.size, 4)
        self.assertEqual(self.ll.get(0), 1)
        self.assertEqual(self.ll.get(1), 2)
        self.assertEqual(self.ll.get(2), 3)
        self.assertEqual(self.ll.get(3), 4)

    def test_add_at_index_beginning(self):
        """Test adding at index 0 (same as addAtHead)"""
        self.ll.addAtTail(2)
        self.ll.addAtTail(3)
        self.ll.addAtIndex(0, 1)
        self.assertEqual(self.ll.size, 3)
        self.assertEqual(self.ll.get(0), 1)
        self.assertEqual(self.ll.get(1), 2)
        self.assertEqual(self.ll.get(2), 3)

    def test_add_at_index_end(self):
        """Test adding at last index (same as addAtTail)"""
        self.ll.addAtTail(1)
        self.ll.addAtTail(2)
        self.ll.addAtIndex(2, 3)
        self.assertEqual(self.ll.size, 3)
        self.assertEqual(self.ll.get(0), 1)
        self.assertEqual(self.ll.get(1), 2)
        self.assertEqual(self.ll.get(2), 3)

    def test_add_at_index_middle(self):
        """Test adding at middle index"""
        self.ll.addAtTail(1)
        self.ll.addAtTail(3)
        self.ll.addAtIndex(1, 2)
        self.assertEqual(self.ll.size, 3)
        self.assertEqual(self.ll.get(0), 1)
        self.assertEqual(self.ll.get(1), 2)
        self.assertEqual(self.ll.get(2), 3)

    def test_add_at_index_invalid(self):
        """Test adding at invalid indices"""
        self.ll.addAtTail(1)
        # Index too large
        self.ll.addAtIndex(5, 99)
        self.assertEqual(self.ll.size, 1)
        # Negative index
        self.ll.addAtIndex(-1, 99)
        self.assertEqual(self.ll.size, 1)

    def test_delete_at_index_single_element(self):
        """Test deleting from single element list"""
        self.ll.addAtTail(1)
        self.ll.deleteAtIndex(0)
        self.assertEqual(self.ll.size, 0)
        self.assertIsNone(self.ll.head)
        self.assertIsNone(self.ll.tail)

    def test_delete_at_index_head(self):
        """Test deleting head element"""
        self.ll.addAtTail(1)
        self.ll.addAtTail(2)
        self.ll.addAtTail(3)
        self.ll.deleteAtIndex(0)
        self.assertEqual(self.ll.size, 2)
        self.assertEqual(self.ll.get(0), 2)
        self.assertEqual(self.ll.get(1), 3)

    def test_delete_at_index_tail(self):
        """Test deleting tail element"""
        self.ll.addAtTail(1)
        self.ll.addAtTail(2)
        self.ll.addAtTail(3)
        self.ll.deleteAtIndex(2)
        self.assertEqual(self.ll.size, 2)
        self.assertEqual(self.ll.get(0), 1)
        self.assertEqual(self.ll.get(1), 2)
        self.assertEqual(self.ll.tail.val, 2)

    def test_delete_at_index_middle(self):
        """Test deleting middle element"""
        self.ll.addAtTail(1)
        self.ll.addAtTail(2)
        self.ll.addAtTail(3)
        self.ll.deleteAtIndex(1)
        self.assertEqual(self.ll.size, 2)
        self.assertEqual(self.ll.get(0), 1)
        self.assertEqual(self.ll.get(1), 3)

    def test_delete_at_index_invalid(self):
        """Test deleting at invalid indices"""
        self.ll.addAtTail(1)
        original_size = self.ll.size
        # Index too large
        self.ll.deleteAtIndex(5)
        self.assertEqual(self.ll.size, original_size)
        # Negative index
        self.ll.deleteAtIndex(-1)
        self.assertEqual(self.ll.size, original_size)

    def test_get_valid_indices(self):
        """Test get with valid indices"""
        for i in range(5):
            self.ll.addAtTail(i * 10)

        for i in range(5):
            self.assertEqual(self.ll.get(i), i * 10)

    def test_get_invalid_indices(self):
        """Test get with invalid indices"""
        self.ll.addAtTail(1)
        self.ll.addAtTail(2)
        # Index too large
        self.assertEqual(self.ll.get(5), -1)
        # Negative index would cause issues in _getNode, but get should handle
        self.assertEqual(self.ll.get(-1), -1)

    def test_complex_operations_sequence(self):
        """Test a complex sequence of operations"""
        # Build list: [1, 2, 3, 4]
        self.ll.addAtHead(2)
        self.ll.addAtTail(3)
        self.ll.addAtHead(1)
        self.ll.addAtTail(4)

        # Insert 5 at index 2: [1, 2, 5, 3, 4]
        self.ll.addAtIndex(2, 5)
        self.assertEqual(self.ll.size, 5)

        # Delete at index 1: [1, 5, 3, 4]
        self.ll.deleteAtIndex(1)
        self.assertEqual(self.ll.size, 4)

        # Verify final state
        self.assertEqual(self.ll.get(0), 1)
        self.assertEqual(self.ll.get(1), 5)
        self.assertEqual(self.ll.get(2), 3)
        self.assertEqual(self.ll.get(3), 4)

    def test_size_consistency(self):
        """Test that size is always consistent"""
        self.assertEqual(self.ll.size, 0)

        self.ll.addAtHead(1)
        self.assertEqual(self.ll.size, 1)

        self.ll.addAtTail(2)
        self.assertEqual(self.ll.size, 2)

        self.ll.addAtIndex(1, 3)
        self.assertEqual(self.ll.size, 3)

        self.ll.deleteAtIndex(0)
        self.assertEqual(self.ll.size, 2)

        self.ll.deleteAtIndex(1)
        self.assertEqual(self.ll.size, 1)

        self.ll.deleteAtIndex(0)
        self.assertEqual(self.ll.size, 0)

    def test_head_tail_consistency(self):
        """Test that head and tail pointers are always correct"""
        # Empty list
        self.assertIsNone(self.ll.head)
        self.assertIsNone(self.ll.tail)

        # Single element
        self.ll.addAtHead(1)
        self.assertIs(self.ll.head, self.ll.tail)

        # Two elements
        self.ll.addAtTail(2)
        self.assertIsNot(self.ll.head, self.ll.tail)
        self.assertEqual(self.ll.head.val, 1)
        self.assertEqual(self.ll.tail.val, 2)

        # Delete back to single element
        self.ll.deleteAtIndex(1)
        self.assertIs(self.ll.head, self.ll.tail)

        # Delete to empty
        self.ll.deleteAtIndex(0)
        self.assertIsNone(self.ll.head)
        self.assertIsNone(self.ll.tail)


if __name__ == "__main__":
    unittest.main()
