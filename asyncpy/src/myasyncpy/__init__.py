from myasyncpy.common import Coroutine, EventLoop

EVENT_LOOP = EventLoop()


def run_loop(coroutine: Coroutine):
    EVENT_LOOP.create_task(coroutine)
    EVENT_LOOP.run_loop()


def create_task(coroutine: Coroutine):
    EVENT_LOOP.create_task(coroutine)
