from collections import defaultdict
from collections.abc import Iterable
from typing import Self, override


class ListNode[T]:
    def __init__(self, val: T):
        self.val: T = val
        self._next: ListNode[T] = self
        self._prev: ListNode[T] = self

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, val: ListNode[T]):
        self._next = val

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, val: ListNode[T]):
        self._prev = val

    @override
    def __str__(self):
        return f"[{self.val}]"


class CircularDoubleLL[T]:
    def __init__(self):
        self._head: ListNode[T]|None = None
        self._count: int = 0
        self._node_table: dict[T,list[ListNode[T]]] = defaultdict(list)

    def add(self, val: ListNode[T]|T):
        if isinstance(val, ListNode):
            newNode: ListNode[T] = val
        else:
            newNode = ListNode(val)

        if self._head is None:
            self._head = newNode
            newNode.next = newNode
            newNode.prev = newNode
        else:
            newNode.next = self._head
            newNode.prev = self._head.prev
            newNode.prev.next = newNode
            newNode.next.prev = newNode
            self._head = newNode
        self._count += 1
        self._node_table[newNode.val].append(newNode)

    def _delete(self, val: ListNode[T]|T):
        node: ListNode[T] 
        if isinstance(val, ListNode):
            node = val
        else:
            if val not in self._node_table or len(self._node_table[val]) == 0:
                raise KeyError
            node = self._node_table[val].pop()

        node.prev.next = node.next
        node.next.prev = node.prev
        if self._head is not None and self._head == node:
            self._head = self._head.next
        self._count -= 1
        # no more refs to node? => garbage collected

    def delete(self, val: list[ListNode[T]|T]|ListNode[T]|T):
        if isinstance(val, list):
            errors = []
            for item in val:
                try:
                    self._delete(item)
                except Exception as e:
                    errors.append(e)

            for e in errors:
                raise e
        else:
            self._delete(val)

    def __iter__(self):
        if self._head == None:
            return None

        current_node: ListNode[T] = self._head
        yield current_node

        while current_node.next != self._head:
            current_node = current_node.next
            yield current_node

    def __len__(self):
        return self._count

    @override
    def __str__(self):
        out = "LinkedList: "
        for node in self:
            out += f'- {str(node)} -'
        return out

