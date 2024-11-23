import cv2

import matplotlib.pyplot as plt
import numpy as np


def load_image(input_image_path: str) -> np.ndarray:
    """
       Считывает изображение из файла и проверяет его.

       :param input_image_path: Путь к файлу изображения.
       :return: Изображение в формате массива NumPy.
       :raise ValueError: Если изображение не удалось загрузить.
       """
    image = cv2.imread(input_image_path)
    if image is None:
        raise ValueError(f"Ошибка: Не удалось загрузить изображение по пути: {input_image_path}")
    return image


def print_image_size(image: np.ndarray) -> None:
    """
    Выводит размер изображения.

    :param image: Изображение в формате массива NumPy.
    """
    height, width, channels = image.shape
    print(f"Размер изображения: {width}x{height} (ширина x высота)")


def plot_histogram(image: np.ndarray) -> list:
    """
    Вычисляет гистограмму цветового распределения изображения.

    :param image: Изображение в формате массива NumPy.
    :return: Список гистограмм для каждого цветового канала.
    """
    histograms = []
    color = ('b', 'g', 'r')  # цвета для гистограммы

    for i in range(3):  # Для каждого цветового канала
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        histograms.append(hist)

    return histograms


def print_histogram(histograms: list) -> None:
    """
    Строит и отображает гистограмму цветового распределения.

    :param histograms: Список гистограмм для каждого цветового канала.
    """
    color = ('b', 'g', 'r')  # цвета для гистограммы
    plt.figure(figsize=(10, 5))

    for i, col in enumerate(color):
        plt.plot(histograms[i], color=col)

    plt.title('Гистограмма изображения')
    plt.xlabel('Интенсивность цвета')
    plt.ylabel('Частота')
    plt.xlim([0, 256])
    plt.grid()
    plt.show()


def invert_colors(image: np.ndarray) -> np.ndarray:
    """
    Инвертирует цвета в изображении.

    :param image: Изображение в формате массива NumPy.
    :return: Инвертированное изображение.
    """
    return cv2.bitwise_not(image)


def display_images(original_image: np.ndarray, inverted_image: np.ndarray) -> None:
    """
    Демонстрирует исходное и инвертированное изображения.

    :param original_image: Исходное изображение в формате массива NumPy.
    :param inverted_image: Инвертированное изображение в формате массива NumPy.
    """
    plt.figure(figsize=(10, 5))

    # Исходное изображение
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
    plt.title('Исходное изображение')
    plt.axis('off')

    # Инвертированное изображение
    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(inverted_image, cv2.COLOR_BGR2RGB))
    plt.title('Инвертированное изображение')
    plt.axis('off')
    plt.show()


def save_image(output_image_path: str, image: np.ndarray) -> None:
    """
    Сохраняет изображение в файл.

    :param output_image_path: Путь для сохранения инвертированного изображения.
    :param image: Изображение в формате массива NumPy.
    """
    cv2.imwrite(output_image_path, image)
