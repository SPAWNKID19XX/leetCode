import asyncio

urls = ["url1","url2","url3","url4","url5"]

async def fetch_mock(url):
    print("Start fetch url ==>",url)
    await asyncio.sleep(0.2)
    return f"{url} --> ok 200"

async def main():
    tasks = [fetch_mock(u) for u in urls]
    l = await asyncio.gather(*tasks)
    print(l)


asyncio.run(main())