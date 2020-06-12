#!/usr/bin/env python3
from bs4 import BeautifulSoup
from pycookiecheat import chrome_cookies
import os
import requests
from shlex import quote

out_dir = "data"

if not os.path.exists(out_dir):
    os.makedirs(out_dir)


cookies = chrome_cookies("https://www.blinkist.com", browser='chromium')
assert cookies is not {}

session = requests.Session()
session.headers.update({"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:74.0) Gecko/20100101 Firefox/74.0"})
session.headers.update({"x-requested-with": "XMLHttpRequest"})
session.cookies.update(cookies)


def download_chapters(link_to_blink):
    resp = session.get(link_to_blink)
    assert resp.status_code == 200, print(resp.text)
    bs = BeautifulSoup(resp.text, 'html.parser')
    blink_name = bs.find("a", {'class': 'share__mail-icon'}).attrs['data-title'].strip()
    data_book_id = bs.find("div", {'class': 'reader__container'}).attrs['data-book-id']
    for i, chapter in enumerate(bs.findAll("li", {'class': 'chapters'})):
        data_chapter_id = chapter.attrs['data-chapterid']
        download_link_tmp = f"https://www.blinkist.com/api/books/{data_book_id}/chapters/{data_chapter_id}/audio"
        resp = session.get(download_link_tmp)
        assert resp.status_code == 200, print(resp.text)
        download_url = resp.json()['url']
        resp = requests.get(download_url)
        assert resp.status_code == 200, print(resp.text)
        output_file = os.path.join(out_dir, f"{blink_name}_{i+1}")
        if os.path.exists(output_file + ".m4a"):
            print("Already there. Skipping")
        else:
            with open(output_file + ".m4a", "wb") as f:
                f.write(resp.content)
        print(f"Downloaded with chapter {i}")
        cmd = f"ffmpeg -v 5 -y -i {quote(output_file)}.m4a -acodec libmp3lame -ac 2 -ab 320k {quote(output_file)}.mp3"
        print(f"Executing {cmd}")
        os.system(cmd)
        print("Converted to mp3")
        print("Deleting m4a file")
        cmd = f"rm {quote(output_file)}.m4a"
        print(f"Executing {cmd}")
        os.system(cmd)


if __name__ == '__main__':
    url = "https://www.blinkist.com/de/nc/reader/how-to-have-impossible-conversations-en"
    download_chapters(url)

