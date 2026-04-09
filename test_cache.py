from functools import lru_cache
import asyncio

@lru_cache
async def get_stuff():
    return "stuff"

async def main():
    print(await get_stuff())
    print(await get_stuff())

asyncio.run(main())
