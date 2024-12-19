import sys
import os

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFileDialog, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from imageiterator import ImageIterator


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        """
        Инициализирует главное окно приложения.

        Устанавливает заголовок окна, размеры и элементы управления.
        """
        super().__init__()

        self.setWindowTitle("Image Dataset Viewer")
        self.setGeometry(100, 100, 800, 600)

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)

        self.next_button = QPushButton("Next Image", self)
        self.next_button.clicked.connect(self.show_next_image)

        self.load_button = QPushButton("Load Dataset", self)
        self.load_button.clicked.connect(self.load_dataset)

        layout = QVBoxLayout()
        layout.addWidget(self.load_button)
        layout.addWidget(self.image_label)
        layout.addWidget(self.next_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.iterator = None

    def load_dataset(self) -> None:
        """
        Загружает файл аннотации и инициализирует итератор изображений.

        Открывает диалог выбора файла для загрузки CSV-файла с аннотациями.
        """
        options = QFileDialog.Options()
        annotation_file, _ = QFileDialog.getOpenFileName(self, "Open Annotation File", "",
                                                         "CSV Files (*.csv);;All Files (*)", options=options)

        if annotation_file:
            self.iterator = ImageIterator(annotation_file)
            self.image_label.clear()
            self.next_button.setEnabled(True)

    def show_next_image(self) -> None:
        """
        Отображает следующее изображение из итератора.

        Если изображение не найдено или больше нет изображений, выводит соответствующее сообщение.
        """
        if self.iterator is not None:
            try:
                image_data = self.iterator.next()
                image_path = image_data[0]
                if os.path.exists(image_path):
                    pixmap = QPixmap(image_path)
                    self.image_label.setPixmap(pixmap.scaled(800, 600, Qt.KeepAspectRatio))
                else:
                    self.image_label.setText("Image not found.")
            except StopIteration:
                self.image_label.setText("No more images.")


def main() -> None:
    """
    Запускает приложение.

    Инициализирует QApplication и главное окно.
    Обрабатывает возможные исключения при запуске.
    """
    try:
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
