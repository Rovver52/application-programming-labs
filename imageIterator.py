import csv

class ImageIterator:
    def __init__(self, annotation_file):
        self.annotation_file = annotation_file
        self.images = self.load_images()

    def load_images(self):
        images = []
        try:
            with open(self.annotation_file, 'r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    images.append(row)
        except FileNotFoundError:
            print(f"Ошибка: Файл {self.annotation_file} не найден.")
        except Exception as e:
            print(f"Ошибка при загрузке изображений: {e}")
        return images

    def __iter__(self):
        return iter(self.images)