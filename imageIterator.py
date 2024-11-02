import csv

class ImageIterator:
    def __init__(self, annotation_file) -> None:
        self.annotation_file = annotation_file
        self.images = self.load_images()

    def load_images(self) -> list[tuple[str, ...]]:
        """
        Collect filenames of downloaded images.
        :param self: Parameter self of imageIterator
        :return: list of filenames in this directory
        """
        images = []
        with open(self.annotation_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Пропускаем заголовок
            for row in reader:
                images.append(tuple(row))
        return images

    def __iter__(self) -> iter:
        return iter(self.images)
