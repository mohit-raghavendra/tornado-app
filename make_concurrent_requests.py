import asyncio
import httpx
import random
import time


async def async_get_calls(url):
    expo = 6
    n = random.randint(1*10**expo, 2*10**expo)
    async with httpx.AsyncClient() as client:
        return await client.get(
            url=url,
            params={"query": n},
            timeout=None
        )


async def launch(urls):
    await asyncio.gather(*map(async_get_calls, urls))


for i in [1, 2, 4, 8, 16, 32, 64]:
    urls = ["http://localhost:8888/pi"]*i
    try:
        tm1 = time.perf_counter()
        asyncio.run(launch(urls))
        tm2 = time.perf_counter()
        print(f'Time for {i} concurrent requsts: {tm2-tm1:0.2f} seconds')
    except Exception as e:
        print(f'Failed for: {i} concurrent requests with {e}')
