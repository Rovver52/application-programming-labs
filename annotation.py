import csv
import os

def create_annotation(imgdir: str,annotation_file: str) -> None:
    """
    Creates annotation with absolute and relative paths to downloaded images
    :param annotation_file: name of file to save annotation
    :param imgdir: directory with saved images
    """
    with open(annotation_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Absolute Path', 'Relative Path'])  # Заголовки

        for filename in os.listdir(imgdir):
            absolute_path = os.path.abspath(os.path.join(imgdir, filename))
            relative_path = os.path.relpath(absolute_path, imgdir)
            writer.writerow([absolute_path, relative_path])
