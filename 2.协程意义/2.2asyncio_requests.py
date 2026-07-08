import asyncio
import aiohttp


async def fetch(session, url):
    print(f"Downloading {url}")
    async with session.get(url) as response:
        content = await response.read()
        file_name = url.split("/")[-1]
        with open(file_name, "wb") as f:
            f.write(content)

async def main():
    async with aiohttp.ClientSession() as session:
        url_list = [
            "https://example.com",
            "https://example.org",
            "https://example.net",
        ]
        tasks = [fetch(session, url) for url in url_list]
        await asyncio.gather(*tasks) # Waiting for all tasks to complete concurrently

if __name__ == "__main__":
    asyncio.run(main())
