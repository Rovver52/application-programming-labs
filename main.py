import argparse
from annotation import create_annotation
from instalImages import install_images
from imageIterator import ImageIterator


def main():
    parser = argparse.ArgumentParser(description='Download images and create an annotation CSV file.')
    parser.add_argument('keyword', type=str, help='Keyword for image search')
    parser.add_argument('imgdir', type=str, help='Directory to save images')
    parser.add_argument('num', type=int, help='Number of images to download (50-1000)', choices=range(50, 1001))
    parser.add_argument('annotate', type=str, help='annotation_file')

    args = parser.parse_args()
    keyword, imgdir, num, annotate = args.keyword, args.imgdir, args.num, args.annotate
    try:
        install_images(keyword, imgdir, num)
        create_annotation(imgdir, annotate)
        image_iterator = ImageIterator(annotate)
        for absolute_path, relative_path in image_iterator:
            print(f'Absolute: {absolute_path}, Relative: {relative_path}')
    except Exception as e:
        print(f"Что-то пошло не так: {e}")


if __name__ == '__main__':
    main()
