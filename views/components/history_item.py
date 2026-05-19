import qtawesome as qta
from PyQt6.QtCore import QMargins, Qt, pyqtSignal
from PyQt6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton
)

# ---- Constants ----
ITEM_WIDTH: int = 880

ITEM_MARGINS: QMargins = QMargins(8,0,8,0)

BTN_WIDTH: int = 35

LBL_MAX_SIZE = 400
# -------------------

class HistoryItem(QFrame):
    del_btn_signal = pyqtSignal(int)
    def __init__(self, name : str, date : str, id : int):
        super().__init__()
        self.name = name
        self.date = date
        self.id = id 

        self._setup_ui()
        self._setup_layout()

    def _setup_ui(self) -> None:
        self.setProperty("class", "history_item")
        self.setMinimumWidth(ITEM_WIDTH)

        self.name_lbl = QLabel(self.name)
        name_fm = self.name_lbl.fontMetrics()
        self.name_lbl.setText(name_fm.elidedText(self.name, Qt.TextElideMode.ElideRight, LBL_MAX_SIZE))
        self.name_lbl.setProperty("class", "hist_item_name")

        self.task_date = QLabel(self.date)
        self.task_date.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.task_date.setProperty("class", "hist_item_date")
        
        self.delete_btn = QPushButton()
        self.delete_btn.setIcon(qta.icon("fa5s.trash"))
        self.delete_btn.setMaximumWidth(BTN_WIDTH)
        self.delete_btn.clicked.connect(lambda : self.del_btn_signal.emit(self.id))
        self.setCursor(Qt.CursorShape.PointingHandCursor)

    def _setup_layout(self) -> None:
        right_layout = QHBoxLayout()
        right_layout.addWidget(self.task_date)
        right_layout.addWidget(self.delete_btn)

        main_layout = QHBoxLayout()
        self.setContentsMargins(ITEM_MARGINS)
        main_layout.addWidget(self.name_lbl)
        main_layout.addLayout(right_layout)

        self.setLayout(main_layout)