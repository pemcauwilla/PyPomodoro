import qtawesome as qta
from PyQt6.QtCore import Qt, QMargins, QSize, pyqtSignal
from PyQt6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QGridLayout,
    QLabel,
    QPushButton
)

# --- Constants ---
ITEM_HEIGHT: int = 40
ITEM_WIDTH: int = 210
ITEM_PADDING: QMargins = QMargins(8,0,4,0)

BTN_ICON_SIZE: QSize = QSize(12,12)
BTN_SPACING: int = 2

LBL_MAX_SIZE: int = 120
# -----------------

class TaskListItem(QFrame):
    def __init__(self, task_name : str, id : int):
        self.task_name = task_name
        self.id = id
        
        super().__init__()
        self._setup_ui()
        self._setup_layouts()

    def _setup_ui(self) -> None:
        self.setMinimumWidth(ITEM_WIDTH)
        self.setFixedHeight(ITEM_HEIGHT)
        self.setProperty("class", "task_item")
    
        self.task_name_lbl = QLabel()
        name_fm = self.task_name_lbl.fontMetrics()
        self.task_name_lbl.setText(name_fm.elidedText(self.task_name, Qt.TextElideMode.ElideRight, LBL_MAX_SIZE))
        self.task_name_lbl.setProperty("class", "task_item_lbl")
        
        self.btn_select_task = QPushButton()
        self.btn_select_task.setIcon(qta.icon("fa5s.check"))
        self.btn_select_task.setIconSize(BTN_ICON_SIZE)
        self.btn_select_task.setProperty("class", "task_item_btn")
        self.btn_select_task.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_select_task.hide()

        self.btn_delete_task = QPushButton()
        self.btn_delete_task.setIcon(qta.icon("fa5s.trash"))
        self.btn_delete_task.setIconSize(BTN_ICON_SIZE)
        self.btn_delete_task.setProperty("class", "task_item_btn")
        self.btn_delete_task.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_delete_task.hide()

        self.empty_frame = QFrame()

    def _setup_layouts(self) -> None:
        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(BTN_SPACING)
        btn_layout.addWidget(self.btn_select_task)
        btn_layout.addWidget(self.btn_delete_task)
        
        main_layout = QGridLayout()
        main_layout.setContentsMargins(ITEM_PADDING)
        main_layout.addWidget(self.task_name_lbl, 0, 1, alignment=Qt.AlignmentFlag.AlignLeft)
        main_layout.addLayout(btn_layout, 0, 2,         alignment=Qt.AlignmentFlag.AlignRight)

        self.setLayout(main_layout)

    def enterEvent(self, event):
        self.btn_delete_task.show()
        self.btn_select_task.show()

    def leaveEvent(self, a0):
        self.btn_delete_task.hide()
        self.btn_select_task.hide()

    