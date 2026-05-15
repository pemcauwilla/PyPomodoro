import sys

from PyQt6.QtWidgets import(
    QApplication
)

from views.main_window import MainWindow
from assets.style_manager import StyleManager

class App():
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.app.setStyleSheet(StyleManager.get_complete_stylesheet())

        self.window = MainWindow()
        
        self.window.show()
        sys.exit(self.app.exec())
        


if __name__ == "__main__":
    app = App()