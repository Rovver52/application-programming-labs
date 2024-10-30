import os
from typing import Optional
from icrawler.builtin import GoogleImageCrawler

def install_images(keyword: str, imgdir: str, num: int) -> Optional[str]:
    """
    This function searches images by keyword in Google and downloads them to the directory. (Clears the directory every time the script is run).
    :param keyword: keyword for searching
    :param num: how many images you want to download
    :param imgdir: directory to save images
    """
    if not os.path.exists(imgdir):
        os.makedirs(imgdir)

    # Очистка директории
    for filename in os.listdir(imgdir):
        os.remove(os.path.join(imgdir, filename))

    try:
        google_crawler = GoogleImageCrawler(downloader_threads=4, storage={'root_dir': imgdir})
        google_crawler.crawl(keyword=keyword, max_num=num)
        return imgdir
    except Exception as e:
        print(f"Произошла ошибка: {e}")
