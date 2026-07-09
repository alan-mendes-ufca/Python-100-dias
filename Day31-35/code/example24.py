"""aiohttp para acesso HTTP assíncrono.
A E/S assíncrona pode lidar com muitas tarefas vinculadas a E/S de forma eficiente com um único loop de eventos."""
import asyncio
import re

import aiohttp


async def fetch(session, url):
    async with session.get(url) as resp:
        resp.raise_for_status()
        return await resp.text()


async def main():
    pattern = re.compile(r'<title>(?P<title>.*?)</title>', re.IGNORECASE | re.DOTALL)
    urls = ('https://www.python.org/',
            'https://git-scm.com/',
            'https://www.jd.com/',
            'https://www.taobao.com/',
            'https://www.douban.com/')
    timeout = aiohttp.ClientTimeout(total=10)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        pages = await asyncio.gather(*(fetch(session, url) for url in urls))
    for html in pages:
        match = pattern.search(html)
        print(match.group('title').strip() if match else 'No title found')


if __name__ == '__main__':
    asyncio.run(main())
