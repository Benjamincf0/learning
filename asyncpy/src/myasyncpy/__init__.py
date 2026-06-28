from collections.abc import Callable, Generator
from functools import wraps
import time
from typing import Any

from .common import Coroutine, EventLoop

EL = EventLoop()


@wraps(EventLoop.run_loop)
def run_loop():
    EL.run_loop()

@wraps(EventLoop.create_task)
def create_task(coroutine):
    EL.create_task(coroutine)

@wraps(EventLoop.gather)
def gather(*coros):
    return EL.gather(*coros)

def __async__[Y, S, R](gen_func: Callable[..., Generator[Y, S, R]]) -> Callable[..., Coroutine[Y, S, R]]:
    def coroutine_factory(*args: Any, **kwargs: Any) -> Coroutine[Y, S, R]:
        return Coroutine(gen_func, *args, **kwargs)
    return coroutine_factory

class sleep:
    def __init__(self, seconds: float):
        self._start: float = time.time()
        self._expected_end: float = self._start + seconds

    def __await__(self) -> Generator[None, None, float]:
        while time.time() < self._expected_end:
            yield
        return time.time() - self._start
