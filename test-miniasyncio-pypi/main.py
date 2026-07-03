import asyncio as io

async def greet(name: str):
    print(f"Hello, {name}!")
    await io.sleep(0.1)
    print(f"Done with {name}")

async def main():
    await io.gather(
        greet("Alice"),
        greet("Bob"),
        greet("Charlie"),
    )

io.run(main())
