import asyncio
import os
import re
from collections import Counter

import aiofiles
import aiohttp
import requests
from bs4 import BeautifulSoup

urls = []
named_files = []


def get_urls() -> None:
    """get urls of flags"""
    resp = requests.get("https://flagi.site/flagi-stran-mira")
    soup = BeautifulSoup(resp.text, 'lxml')
    urls.extend(
        [flag.get('data-src') for flag in soup.find_all(width="64")[::2]]
    )
    named_files = re.findall(r'\w+\.(?:png|jpeg)', ' '.join(urls))
    print(Counter(urls))
    print(len(urls))
    print(len(named_files))
\.(?:png|jpeg|jpg|gif)
async def download_url(url: str, filename: str) -> None:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status_code == 200:
                f = await aiofiles.open(f"/flags/{filename}", mode='wb')
                await f.write(await resp.read())
                await f.close()


async def main():
    # coros = [download_url() for ]
    # await get_urls()
    get_urls()
    return 0


if __name__ == '__main__':
    os.getcwd()
    try:
        os.mkdir('flags')
    except OSError:
        print("Folder flags is created")
    loop = asyncio.get_event_loop()
    status = loop.run_until_complete(main())
    # main()
