from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def _getNode(self, index: int) -> Optional[ListNode]:
        if index < 0:
            return None
        curr = self.head
        while index > 0:
            if not curr:
                return None
            curr = curr.next
            index -= 1
        return curr

    def get(self, index: int) -> int:
        node = self._getNode(index)
        if node:
            return node.val
        return -1

    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        node.next = self.head
        self.head = node
        if not self.tail:
            self.tail = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        node = ListNode(val)
        if self.tail:
            self.tail.next = node
        self.tail = node
        if not self.head:
            self.head = node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size or index < 0:
            return
        if index == 0:
            return self.addAtHead(val)
        if index == self.size:
            return self.addAtTail(val)
        new_node = ListNode(val)
        node = self._getNode(index - 1)
        new_node.next = node.next
        node.next = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size or index < 0:
            return
        self.size -= 1
        if index == 0:
            self.head = self.head.next
            if self.size == 0:
                self.tail = None
        else:
            node = self._getNode(index - 1)
            node.next = node.next.next
            if index == self.size:
                self.tail = node
