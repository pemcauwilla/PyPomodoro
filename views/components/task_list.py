from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QFrame,
    QScrollArea,
    QVBoxLayout
)

# ONLY FOR TESTING
from .task_list_item import TaskListItem

class TaskList(QScrollArea):
    def __init__(self):
        super().__init__()
        self._setup_ui()
        self._setup_layout()

    def _setup_ui(self) -> None:
        self.inner_widget = QFrame()
        self.setWidgetResizable(True)

    def _setup_layout(self) -> None:
        self.inner_layout =  QVBoxLayout()
        self.inner_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # MOCK DATA
        self.inner_layout.addWidget(TaskListItem("Test"))

        self.inner_widget.setLayout(self.inner_layout)

        self.setWidget(self.inner_widget)