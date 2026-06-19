from myasyncpy.example import EventLoop, Coroutine

EVENT_LOOP = EventLoop()


def run(coroutine: Coroutine):
    EVENT_LOOP.create_task(coroutine)
    EVENT_LOOP.run_loop()


def create_task(coroutine: Coroutine):
    EVENT_LOOP.create_task(coroutine)
