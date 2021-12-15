import concurrent.futures
import os
import re
import time
import typing
from collections import Counter
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


def download_url(url: str, filename: str) -> None:
    resp = requests.get(url)
    if resp.status_code == 200:
        with open(f'flags/{filename}', mode="wb") as f:
            f.write(resp.content)


def main_concurrent() -> None:
    """multithreading or asyncore"""
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        futures.extend([
            executor.submit(download_url, url, filename) for url, filename
            in get_urls()
        ])
        start = time.time()
        result = [_ for _ in concurrent.futures.as_completed(futures)]
        end = time.time()
        print(f"Threading:  {end - start}")


def main_native() -> None:
    """only one thread"""
    start = time.time()
    for url, filename in get_urls():
        download_url(url, filename)
    end = time.time()
    print(f"Native:  {end - start}")


if __name__ == '__main__':
    try:
        os.mkdir('flags')
    except OSError:
        print("Folder flags is created")
    main_concurrent()
    # main_native()
