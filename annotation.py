import csv
import os
from typing import Optional

def create_annotation(imgdir: str) -> Optional[str]:
    """
    Creates annotation with absolute and relative paths to downloaded images
    :param imgdir: directory with saved images
    """
    annotation_file = os.path.join(imgdir, 'annotation.csv')
    try:
        with open(annotation_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Absolute Path', 'Relative Path'])  # Заголовки

            for filename in os.listdir(imgdir):
                absolute_path = os.path.abspath(os.path.join(imgdir, filename))
                relative_path = os.path.relpath(absolute_path, imgdir)
                writer.writerow([absolute_path, relative_path])

        return annotation_file

    except Exception as e:
        print(f"Ошибка при создании аннотации: {e}")