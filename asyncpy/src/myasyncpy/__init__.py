import time

from myasyncpy.common import Coroutine, EventLoop

EVENT_LOOP = EventLoop()


def run_loop():
    EVENT_LOOP.run_loop()

def create_task(coroutine: Coroutine):
    EVENT_LOOP.create_task(coroutine)

def sleep(time_s: float):
    start_time = time.time()
    end_time = start_time + time_s
    while time.time() < end_time:
        EVENT_LOOP.run_loop()
