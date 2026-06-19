from collections.abc import Iterable, Iterator
from enum import Enum, auto
from statistics import _SizedIterable
from types import NoneType
from typing import Self, cast, override
from .linkedlist import ListNode, CircularDoubleLL
from .common import Coroutine

class TaskState(Enum):
    READY = auto()
    RUNNING = auto()
    PAUSED = auto()
    FINISHED = auto()

class Task(ListNode[NoneType]):
    def __init__(self, coroutine: Coroutine):
        super().__init__(val = None)
        self.state: TaskState = TaskState.READY
        self.coroutine: Coroutine = coroutine

class TaskQueue[T](CircularDoubleLL[T], Iterable[T], Iterator[T], _SizedIterable):
    def __init__(self):
        super().__init__()
        self._iter_current: Task|None = None

    def enqueue(self, task: T):
        self.add(task)

    def dequeue(self, task: Task):
        listNode = cast(ListNode[T], task)
        self.deleteNode(listNode)

    @override
    def __len__(self):
        return self._count

    @override
    def __iter__(self) -> Self:
        return self

    @override
    def __next__(self) -> T:
        return self._iter_current.next
