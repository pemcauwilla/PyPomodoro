from dataclasses import dataclass

from PyQt6.QtWidgets import(
    QMainWindow,
    QStackedWidget
)
from PyQt6.QtCore import(
    QSize
)

from .pomodoro_view import PomodoroView

# ---- Constants ----
WINDOW_HEIGHT: int = 960
WINDOW_WIDTH: int = 600
WINDOW_TITLE: str = "Pomodoro Timer"
# -------------------

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setFixedSize(QSize(WINDOW_HEIGHT,WINDOW_WIDTH))
        self.setWindowTitle(WINDOW_TITLE)

        self._setup_ui()
        self._setup_layout()

    def _setup_ui(self) -> None:
        self.pom_view = PomodoroView()

        self.central_widget = QStackedWidget()   

    def _setup_layout(self) -> None:
        self.central_widget.addWidget(self.pom_view)
        self.setCentralWidget(self.central_widget)