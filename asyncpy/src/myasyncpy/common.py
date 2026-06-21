from enum import auto, Enum
from typing import Callable
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

class Myfuture[FutureResult]:
    """ Resolves sometime in the future """
    def __init__(self):
        self.result: FutureResult = None

    def resolve(self, result: FutureResult):
        self.result = result

    def get_result(self):
        return self.result

class Coroutine:
    """ Awaitable object """
    def __init__[T, O](self, func: Callable[[T], O]) -> None:
        super().__init__()
        self.func: Callable[[T], O] = func
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
        while len(self.taskQueue) > 0:
            currentNode = self.taskQueue.dequeue()
            currentTask = currentNode.val
            currentTask.coroutine.func()

    def create_task(self, coroutine: Coroutine):
        """ Add task to event loop """
        task = Task(coroutine)
        self._add_task(task)

    def _add_task(self, task: Task):
        self.taskQueue.add(task)
