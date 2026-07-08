import aiohttp
import asyncio

async def fetch(session,url):
    async with session.get(url,verify_ssl=False) as resp:
        text = await resp.text()
        print('result:',url,len(text))

async def main():
    url_list = [
        'https://www.baidu.com',
        'https://www.taobao.com',
        'https://www.jd.com',
        'https://www.sina.com.cn',
        'https://www.sohu.com',
    ]
    async with aiohttp.ClientSession() as session:
        tasks = [
            fetch(session, url) for url in url_list
        ]
        await asyncio.gather(*tasks)



if __name__ == '__main__':
    asyncio.run(main())