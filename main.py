import argparse

from worktofile import load_image, print_image_size, plot_histogram, invert_colors, display_images, save_image


def main(input_image_path: str, output_image_path: str) -> None:
    """
    Основная функция обработки изображения.

    :param input_image_path: Путь к входному изображению.
    :param output_image_path: Путь для сохранения инвертированного изображения.
    """
    try:

        image = load_image(input_image_path)
        print_image_size(image)
        plot_histogram(image)
        inverted_image = invert_colors(image)
        display_images(image, inverted_image)
        save_image(output_image_path, inverted_image)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Обработка изображения: инверсия цветов и построение гистограммы.")

    parser.add_argument("input_image", help="Путь к входному изображению")
    parser.add_argument("output_image", help="Путь для сохранения инвертированного изображения")

    args = parser.parse_args()

    main(args.input_image, args.output_image)