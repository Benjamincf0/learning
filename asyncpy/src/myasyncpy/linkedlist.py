from typing import Self


class ListNode[T]:
    def __init__(self, val: T):
        self._val: T = val
        self._next: ListNode[T]
        self._prev: ListNode[T]

    @property
    def next(self) -> Self:
        return self._next

    @next.setter
    def next(self, val: Self|T):
        if isinstance(val, ListNode):
            self._next = val
        else:
            self._next = ListNode(val)

    @property
    def prev(self) -> Self:
        return self._next

    @prev.setter
    def prev(self, val: Self|T):
        if isinstance(val, ListNode):
            self._prev = val
        else:
            self._prev = ListNode(val)


class CircularDoubleLL[T]:
    def __init__(self):
        self._head: ListNode[T]|None = None
        self._count: int = 0

    def add(self, val: ListNode[T]|T):
        if isinstance(val, ListNode):
            newNode: ListNode[T] = val
        else:
            newNode = ListNode(val)

        if self._head is None:
            self._head = newNode
            newNode.next = self._head
            newNode.prev = self._head.prev
        else:
            newNode.next = self._head
            newNode.prev = self._head.prev
            newNode.prev.next = newNode
            newNode.next.prev = newNode
        self._count += 1

    def deleteNode(self, node: ListNode[T]):
        node.prev.next = node.next
        node.next.prev = node.prev
        self._count -= 1
        # no more refs to node? => garbage collected
