import sys

from PyQt6.QtWidgets import(
    QApplication
)

from views.main_window import MainWindow
from assets.style_manager import StyleManager
from controllers.main_controller import MainViewController
from models.task_model import TaskModel

class App():
    def __init__(self):
        app = QApplication(sys.argv)
        app.setStyleSheet(StyleManager.get_complete_stylesheet())
        model = TaskModel()
        window = MainWindow(model)
        main_controller = MainViewController(view=window, model=model)
        window.show()
        sys.exit(app.exec())
        

if __name__ == "__main__":
    app = App()