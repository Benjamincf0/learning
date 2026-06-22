from collections.abc import Generator
from enum import auto, Enum
from typing import Callable, ParamSpec, TypeVar
from .linkedlist import CircularDoubleLL

class TaskState(Enum):
    READY = auto()
    RUNNING = auto()
    PAUSED = auto()
    FINISHED = auto()

class Task:
    def __init__(self, coroutine: Coroutine):
        self.state: TaskState = TaskState.READY
        self.coroutine: Coroutine = coroutine

class TaskQueue[T](CircularDoubleLL[T]):
    def __init__(self):
        super().__init__()

    def enqueue(self, task: T):
        self.add(task)

    def dequeue(self):
        it = iter(self)
        return next(it)

class Myfuture:
    """ Resolves sometime in the future """
    def __init__(self):
        self.result: FutureResult|None = None

    def resolve(self, result: FutureResult):
        self.result = result

    def get_result(self):
        return self.result


P = ParamSpec("P")
R = TypeVar("R")

class Coroutine:
    """ Awaitable object """
    def __init__(self, func: Callable[P, R]) -> None:
        def func_generator():
            yield func()

        if isinstance(func, Generator):
            func_generator = func

        self.generator: Generator = func_generator()
        self.future: Myfuture = Myfuture()

    def __await__(self) -> Myfuture:
        return Myfuture()


class EventLoop:
    """Main orchestrator"""
    unique_instance: EventLoop|None = None

    def __init__(self):
        if self.unique_instance is not None:
            return self.unique_instance

        self.taskQueue: TaskQueue[Task] = TaskQueue()

    def run_loop(self):
        """ Runs until loop is empty """
        for node in self.taskQueue.iter_forever():
            task = node.val
            if task.state == TaskState.RUNNING:
                continue
            else:
                task.state = TaskState.RUNNING
            try:
                next(task.coroutine.generator)
            except StopIteration:
                task.state = TaskState.FINISHED
                self.taskQueue.delete(node)

    def run_next(self):
        """ Runs until loop is empty using recursion """
        # Run next item in event task Queue.
        nextNode = self.taskQueue.advance()
        if nextNode is None: # exit condition
            return

        task = nextNode.val
        try:
            next(task.coroutine.generator)
        except StopIteration:
            self.taskQueue.delete(nextNode)

    def create_task(self, coroutine: Coroutine):
        """ Add task to event loop """
        task = Task(coroutine)
        self.taskQueue.add(task)
