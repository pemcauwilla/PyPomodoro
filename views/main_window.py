from typing import Callable

from PyQt6.QtWidgets import(
    QMainWindow,
    QStackedWidget,
    QPushButton
)
from PyQt6.QtCore import(
    QSize
)

from .pomodoro_view import PomodoroView
from .history_view import HistoryView

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
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        self.pom_view = PomodoroView()
        self.hist_view = HistoryView()

        self.central_widget = QStackedWidget()   

    def _setup_layout(self) -> None:
        self.central_widget.addWidget(self.pom_view)
        self.central_widget.addWidget(self.hist_view)
        self.setCentralWidget(self.central_widget)

    def bind_btn_clicked(self, btn : QPushButton, action : Callable) -> None:
        btn.clicked.connect(action)

