from enum import Enum, auto
from typing import Any, Callable

type FutureResult = Any  # pyright: ignore[reportExplicitAny]

class Myfuture:
    """ Resolves sometime in the future """
    def __init__(self):
        self.result: FutureResult = None

    def resolve(self, result: FutureResult):
        self.result = result

    def get_result(self):
        return self.result

class Coroutine:
    def __init__[T, O](self, func: Callable[[T], O]) -> None:
        super().__init__()
        self.func: Callable = func  # pyright: ignore[reportMissingTypeArgument]
        self.future: Myfuture = Myfuture()


# can only be 1
class EventLoop:

    def __init__(self):
        self.taskQueue: list[Task|None] = []
        ...

    def run_loop(self):
        """ Runs until loop is empty """
        while len(self.taskQueue) > 0:
            pass


    def create_task(self, coroutine: Coroutine):
        """ Add task to event loop """
        task = Task(coroutine)
        self._add_task(task)

    def _add_task(self, task: Task):
        self.taskQueue.append(task)

def async_decorator[T, O](func: Callable[[T], O]) -> Coroutine:
    return Coroutine(func)
