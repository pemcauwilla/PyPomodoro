from dataclasses import dataclass

from PyQt6.QtWidgets import(
    QMainWindow,
    QStackedWidget
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
        self._connect_signals()

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

    def _connect_signals(self) -> None:
        self.pom_view.task_history_btn.clicked.connect(self._change_view)
        self.hist_view.back_btn.clicked.connect(self._change_view)

    def _change_view(self) -> None:
        self.central_widget.setCurrentIndex(1 - self.central_widget.currentIndex())