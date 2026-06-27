from collections.abc import Callable
from functools import wraps
import time

from .common import Coroutine, EventLoop

EVENT_LOOP = EventLoop()


@wraps(EventLoop.run_loop)
def run_loop():
    EVENT_LOOP.run_loop()

@wraps(EventLoop.create_task)
def create_task(coroutine: Coroutine):
    EVENT_LOOP.create_task(coroutine)

def sleep(time_s: float) -> Callable[[], bool]:
    """ Factory that creates an elapsed-time tester function """
    start_time = time.time()
    def is_sleep_over():
        if time.time() - start_time >= time_s:
            return True
        return False
    return is_sleep_over
