from collections.abc import Callable, Coroutine, Generator
import time

import myasyncpy as aio
import asyncio as aio2

@aio.__async__
def doStuff(c: str, secs: float) -> Generator[None, None, str]:
    print("Starting", c)
    actual_sleep_time = yield from aio.sleep(secs).__await__()
    print("Finished", c, "after", actual_sleep_time)
    return f'Coro {c} result'

async def doStuffAsync(c: str, secs: float) -> str:
    print("Starting", c)
    actual_sleep_time = await aio.sleep(secs)
    print("Finished", c, "after", actual_sleep_time)
    return f'Coro {c} result'

@aio.__async__
def main():
    print("\n\nStandard coroutine object:")
    start = time.time()
    results = yield from aio.gather(doStuffAsync('A', 0.3), doStuffAsync('B', 0.2), doStuffAsync('C', 0.1)).__await__()
    print(results)
    print('Ran all coros in', time.time()-start, 'seconds')

async def mainAsync():
    print("\n\nStandard coroutine object:")
    start = time.time()
    results = await aio2.gather(doStuffAsync('A', 0.3), doStuffAsync('B', 0.2), doStuffAsync('C', 0.1))
    print(results)
    print('Ran all coros in', time.time()-start, 'seconds')


if __name__ == "__main__":
    aio.run(main())
    aio2.run(mainAsync())
