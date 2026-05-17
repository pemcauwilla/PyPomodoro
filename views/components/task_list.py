from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QFrame,
    QScrollArea,
    QVBoxLayout
)

# ----- Constants -----

# ---------------------

# ONLY FOR TESTING
from .task_list_item import TaskListItem
from .history_item import HistoryItem

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
        self.inner_layout.addWidget(HistoryItem("TestAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"))
        self.inner_layout.addWidget(HistoryItem("Test"))
    
        self.inner_widget.setLayout(self.inner_layout)

        self.setWidget(self.inner_widget)