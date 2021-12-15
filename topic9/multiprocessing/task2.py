import multiprocessing
import os
import re
import time
import typing
from collections import Counter
import requests
from PIL import Image, ImageOps
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


def make_cornice_multi(filename: str) -> None:
    img = Image.open(f'flags/{filename}')
    img_border = ImageOps.expand(img, border=100, fill='black')
    img_border.save(f'flags_plus_multi/{filename}')


def make_cornice_native(filename: str) -> None:
    img = Image.open(f'flags/{filename}')
    img_border = ImageOps.expand(img, border=100, fill='black')
    img_border.save(f'flags_plus_native/{filename}')


def main_multiprocessing() -> None:
    """multiprocessing"""
    start = time.time()
    with multiprocessing.Pool(6) as p:
        p.map(make_cornice_multi, [filename[1] for filename in get_urls()])
    end = time.time()
    print(f"multiprocessing: {end - start}")


def main_native() -> None:
    """only one process"""
    start = time.time()
    for filename in get_urls():
        make_cornice_native(filename[1])
    end = time.time()
    print(f"native: {end - start}")


if __name__ == '__main__':
    try:
        os.mkdir("flags_plus_multi")
    except IOError:
        print("folder flags_plus_multi is exist")
    try:
        os.mkdir("flags_plus_native")
    except IOError:
        print("folder flags_pus_native is exist")
    main_multiprocessing()
    main_native()
