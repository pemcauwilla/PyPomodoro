from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QFrame,
    QScrollArea,
    QVBoxLayout
)

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
        
        self.inner_widget.setLayout(self.inner_layout)

        self.setWidget(self.inner_widget)

    def load_list(self, item_list : list[QFrame]) -> None:
        self._clear_layout()        

        for item in item_list:
            self.inner_layout.addWidget(item)

    def _clear_layout(self) -> None:
        while self.inner_layout.count():
            item = self.inner_layout.takeAt(0)
            widget = item.widget()
            
            if widget is not None:
                widget.deleteLater()