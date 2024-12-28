import argparse
import cv2
import pandas as pd
from matplotlib import pyplot as plt


def calculate_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Вычисляет статистическую информацию о размерах изображений.

    :param df: DataFrame с размерами изображений.
    :return: DataFrame со статистикой.
    """
    return df[['height', 'width', 'depth']].describe()

def filter_images(df: pd.DataFrame, max_width: int, max_height: int) -> pd.DataFrame:
    """
    Фильтрует DataFrame по максимальным значениям ширины и высоты.

    :param df: DataFrame с изображениями.
    :param max_width: Максимальная ширина для фильтрации.
    :param max_height: Максимальная высота для фильтрации.
    :return: Отфильтрованный DataFrame.
    """
    return df[(df['height'] <= max_height) & (df['width'] <= max_width)]

def get_image_size(image_path: str) -> Tuple[Optional[int], Optional[int], Optional[int]]:
    """
    Получает размеры изображения (высота, ширина, глубина) по заданному пути.

    :param image_path: Путь к изображению.
    :return: Кортеж с высотой, шириной и глубиной изображения или (None, None, None) в случае ошибки.
    """
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Ошибка: Не удалось загрузить изображение по пути: {image_path}")

    height, width = img.shape[:2]
    depth = img.shape[2] if len(img.shape) > 2 else 1  # Глубина (количество каналов)
    return height, width, depth

def load_annotations(annotation_file: str) -> pd.DataFrame:
    """
    Загружает аннотации из CSV файла.

    :param annotation_file: Путь к CSV файлу с аннотациями.
    :return: DataFrame с аннотациями.
    """
    return pd.read_csv(annotation_file, header=0, names=['absolute_path', 'relative_path'])


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
    
    
def update_image_sizes(df: pd.DataFrame) -> pd.DataFrame:
    """
    Обновляет DataFrame с размерами изображений.

    :param df: DataFrame с аннотациями изображений.
    :return: Обновленный DataFrame с размерами изображений.
    """
    sizes = df['absolute_path'].apply(get_image_size)
    sizes = sizes.dropna()  # Удаление строк с ошибками
    df[['height', 'width', 'depth']] = pd.DataFrame(sizes.tolist(), index=sizes.index)

    # Создание нового столбца для площади изображения
    df['area'] = df['height'] * df['width']

    return df


def main() -> None:
    """
    Основная функция для загрузки данных об изображениях и их анализа.
    """
    parser = argparse.ArgumentParser(description='Парсер для загрузки данных об изображениях.')
    parser.add_argument('annotation_file', type=str, help='Путь к CSV файлу с аннотациями')
    parser.add_argument('max_width', type=int, help='Максимальная ширина для фильтрации')
    parser.add_argument('max_height', type=int, help='Максимальная высота для фильтрации')

    args = parser.parse_args()
    try:
        df = load_annotations(args.annotation_file)

        df = update_image_sizes(df)

        stats = calculate_statistics(df)
        print("Статистическая информация о размерах изображений:")
        print(stats)

        filtered_df = filter_images(df, args.max_width, args.max_height)
        print("\nОтфильтрованный DataFrame:")
        print(filtered_df)

        df_sorted = df.sort_values(by='area')
        print("\nОтсортированный DataFrame по площади изображений:")
        print(df_sorted)

        plot_area_distribution(df_sorted)
    except Exception as e:
        print(f"Что-то пошло не так {e}")


if __name__ == "__main__":
    main()
