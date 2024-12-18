import csv

class ImageIterator:
    def __init__(self, annotation_file: str) -> None:
        """
        Инициализирует итератор изображений.

        :param annotation_file: Путь к файлу аннотации (CSV), содержащему пути к изображениям.
        """
        self.counter = 0
        self.annotation_file = annotation_file
        self.images = self.load_images()

    def load_images(self) -> list[tuple[str, ...]]:
        """
        Загружает изображения из файла аннотации.

        :return: Список кортежей, представляющих строки из файла аннотации.
        """
        images = []
        with open(self.annotation_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Пропускаем заголовок
            for row in reader:
                images.append(tuple(row))
        return images

    def __iter__(self) -> iter:
        """
        Возвращает итератор для изображений.

        :return: Итератор по списку изображений.
        """
        return iter(self.images)

    def next(self) -> tuple[str, ...]:
        """
        Возвращает следующую строку с изображением из списка.

        :return: Кортеж с данными следующего изображения.
        :raises StopIteration: Если больше нет изображений для отображения.
        """
        if self.counter < len(self.images):
            result = self.images[self.counter]
            self.counter += 1
            return result
        else:
            raise StopIteration