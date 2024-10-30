import argparse
from instalImages import install_images
from imageIterator import ImageIterator
from annotation import create_annotation

def main():
    parser = argparse.ArgumentParser(description='Download images and create an annotation CSV file.')
    parser.add_argument('keyword', type=str, help='Keyword for image search')
    parser.add_argument('imgdir', type=str, help='Directory to save images')
    parser.add_argument('num', type=int, help='Number of images to download (50-1000)', choices=range(50, 1001))

    args = parser.parse_args()
    try:

        imgdir = install_images(args.keyword, args.imgdir, args.num)

        if imgdir:
            print(f'Images downloaded to {imgdir}')

            annotation_file = create_annotation(imgdir)

            if annotation_file:
                print(f'Annotation saved to {annotation_file}')

            # Пример использования итератора
                image_iterator = ImageIterator(annotation_file)
                for absolute_path, relative_path in image_iterator:
                    print(f'Absolute: {absolute_path}, Relative: {relative_path}')
    except Exception as e:
        print(f"Что-то пошло не так: {e} ")


if __name__ == '__main__':
    main()
