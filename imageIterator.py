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
        try:
            with open(self.annotation_file, 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Пропускаем заголовок
                for row in reader:
                    images.append(tuple(row))
        except FileNotFoundError:
            print(f"Ошибка: Файл {self.annotation_file} не найден.")
        except Exception as e:
            print(f"Ошибка при загрузке изображений: {e}")
        return images

    def __iter__(self) -> iter:
        return iter(self.images)
