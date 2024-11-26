import argparse
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from typing import Tuple, Optional


def get_image_size(image_path: str) -> Tuple[Optional[int], Optional[int], Optional[int]]:
    """
    Получает размеры изображения (высота, ширина, глубина) по заданному пути.

    :param image_path: Путь к изображению.
    :return: Кортеж с высотой, шириной и глубиной изображения или (None, None, None) в случае ошибки.
    """
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            depth = len(img.getbands())  # Количество каналов
        return height, width, depth
    except Exception as e:
        print(f"Ошибка при обработке изображения {image_path}: {e}")
        return None, None, None


def filter_images(df: pd.DataFrame, max_width: int, max_height: int) -> pd.DataFrame:
    """
    Фильтрует DataFrame по максимальным значениям ширины и высоты.

    :param df: DataFrame с изображениями.
    :param max_width: Максимальная ширина для фильтрации.
    :param max_height: Максимальная высота для фильтрации.
    :return: Отфильтрованный DataFrame.
    """
    return df[(df['height'] <= max_height) & (df['width'] <= max_width)]


def calculate_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Вычисляет статистическую информацию о размерах изображений.

    :param df: DataFrame с размерами изображений.
    :return: DataFrame со статистикой.
    """
    return df[['height', 'width', 'depth']].describe()


def plot_area_distribution(df: pd.DataFrame) -> None:
    """
    Строит гистограмму распределения площадей изображений.

    :param df: DataFrame с размерами изображений.
    """
    plt.figure(figsize=(10, 6))
    plt.hist(df['area'], bins=20, color='blue', alpha=0.7)
    plt.title('Распределение площадей изображений')
    plt.xlabel('Площадь изображения (пиксели)')
    plt.ylabel('Количество изображений')
    plt.grid(axis='y', alpha=0.75)
    plt.show()


def main() -> None:
    """
    Основная функция для загрузки данных об изображениях и их анализа.
    """
    parser = argparse.ArgumentParser(description='Парсер для загрузки данных об изображениях.')
    parser.add_argument('annotation_file', type=str, help='Путь к CSV файлу с аннотациями')
    parser.add_argument('max_width', type=int, help='Максимальная ширина для фильтрации')
    parser.add_argument('max_height', type=int, help='Максимальная высота для фильтрации')

    args = parser.parse_args()

    annotation_file, max_width, max_height = args.annotation_file, args.max_width, args.max_height

    df = pd.read_csv(annotation_file, header = 0, names=['absolute_path', 'relative_path'])

    # Применение функции к каждому изображению в DataFrame
    sizes = df['absolute_path'].apply(get_image_size)
    sizes = sizes.dropna()  # Удаление строк с ошибками

    # Обновление DataFrame с полученными размерами
    df[['height', 'width', 'depth']] = pd.DataFrame(sizes.tolist(), index=sizes.index)

    # Вычисление статистической информации
    stats = calculate_statistics(df)
    print("Статистическая информация о размерах изображений:")
    print(stats)

    # Фильтрация изображений по заданным максимальным размерам
    filtered_df = filter_images(df, max_width, max_height)
    print("\nОтфильтрованный DataFrame:")
    print(filtered_df)

    # Создание нового столбца для площади изображения
    df['area'] = df['height'] * df['width']

    # Сортировка DataFrame по площади изображений
    df_sorted = df.sort_values(by='area')
    print("\nОтсортированный DataFrame по площади изображений:")
    print(df_sorted)

    # Построение гистограммы распределения площадей изображений
    plot_area_distribution(df_sorted)


if __name__ == "__main__":
    main()