import argparse

from worktofile import load_image, print_image_size, plot_histogram, invert_colors, display_images, save_image, print_histogram


def main() -> None:
    """
    Основная функция обработки изображения.
    """
    parser = argparse.ArgumentParser(description="Обработка изображения: инверсия цветов и построение гистограммы.")

    parser.add_argument("input_image", help="Путь к входному изображению")
    parser.add_argument("output_image", help="Путь для сохранения инвертированного изображения")

    args = parser.parse_args()
    input_image_path, output_image_path = args.input_image, args.output_image
    try:

        image = load_image(input_image_path)
        print_image_size(image)
        plot_histogram(image)
        print_histogram()
        inverted_image = invert_colors(image)
        display_images(image, inverted_image)
        save_image(output_image_path, inverted_image)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
