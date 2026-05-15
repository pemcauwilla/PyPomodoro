import sys

from PyQt6.QtWidgets import(
    QApplication
)

from views.main_window import MainWindow

class App():
    def __init__(self):
        self.app = QApplication(sys.argv)
        
        self.window = MainWindow()
        
        self.window.show()
        sys.exit(self.app.exec())
        

        print("rodei?")

if __name__ == "__main__":
    app = App()