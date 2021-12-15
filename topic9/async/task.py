import asyncio
import os
import re
import time
import typing
from collections import Counter

import aiofiles
import aiohttp
import requests
from bs4 import BeautifulSoup


def get_urls() -> typing.List[typing.Tuple[str, str]]:
    """get urls and filenames of flags"""
    resp = requests.get("https://flagi.site/flagi-stran-mira")
    soup = BeautifulSoup(resp.text, 'lxml')
    urls = []
    urls.extend(
        [flag.get('data-src') for flag in soup.find_all(width="64")[::2]]
    )
    named_files = re.findall(r'[a-zA-Z0-9-]*\.(?:png|jpeg|jpg|gif)',
                             ' '.join(urls))
    print("log get_urls:")
    print(">>>>")
    print(Counter(urls))
    print(len(urls))
    print(len(named_files))
    print("<<<<")
    return list(zip(urls, named_files))


async def download_url(url: str, filename: str) -> None:
    """download flags"""
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                f = await aiofiles.open(f"flags/{filename}", mode='wb')
                await f.write(await resp.read())
                await f.close()
                print(f"write {filename}")


async def main() -> None:
    coros = [download_url(url, filename) for url, filename in get_urls()]
    start = time.time()
    await asyncio.gather(*coros)
    end = time.time()
    print(end - start)


if __name__ == '__main__':
    try:
        os.mkdir('flags')
    except OSError:
        print("Folder flags is created")
    loop = asyncio.get_event_loop()
    status = loop.run_until_complete(main())
