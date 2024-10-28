from icrawler.builtin import GoogleImageCrawler
import os
import csv

def install_images(keyword, imgdir, num):
    if not os.path.exists(imgdir):
        os.makedirs(imgdir)

    # Очистка директории
    try:
        for filename in os.listdir(imgdir):
            os.remove(os.path.join(imgdir, filename))
    except Exception as e:
        print(f"Ошибка при очистке директории: {e}")

    try:
        google_crawler = GoogleImageCrawler(downloader_threads=4, storage={'root_dir': imgdir})
        google_crawler.crawl(keyword=keyword, max_num=num)

        # Создание аннотации
        annotation_file = os.path.join(imgdir, 'annotation.csv')
        with open(annotation_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Absolute Path', 'Relative Path'])  # Заголовки

            for filename in os.listdir(imgdir):
                absolute_path = os.path.abspath(os.path.join(imgdir, filename))
                relative_path = os.path.relpath(absolute_path, imgdir)
                writer.writerow([absolute_path, relative_path])

        return annotation_file

    except Exception as e:
        print(f"Произошла ошибка: {e}")