from typing import Callable

import qtawesome as qta
from PyQt6.QtCore import Qt, QMargins, QSize, QDate
from PyQt6.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QLineEdit,
    QPushButton,
    QCheckBox,
    QWidget,
    QComboBox,
    QDateEdit
)

from models.task_model import TaskModel
from .components.task_list import TaskList
from .components.history_item import HistoryItem

# ---- Constants -----
# Window Spacings
HISTORY_MARGINS: QMargins = QMargins(30,30,30,30,)

# Main Layout Spacings
MAIN_MARGINS: QMargins = QMargins(0,0,0,0)

# Header Spacings
HEADER_MARGINS: QMargins = QMargins(15,5,15,0)
HEADER_HEIGHT: int = 70

# Header Measures
INPUT_SIZE: QSize  = QSize(350, 35)

# Button Measures
BTN_ICON_SIZE: QSize = QSize(18,18)
BACK_ICON_SIZE: QSize = QSize(14,14)

BTN_WIDTH: int = 50
BACK_BTN_WIDTH: int = 35

# CheckBox + ComboBox Spacings
CC_SPACING: int = 25

# Task History Spacings
TASK_LIST_WIDTH: int = 540

TASK_LIST_MARGINS: QMargins = QMargins(5,5,5,5)
TASK_LIST_SPACING: int = 5
# --------------------

class HistoryView(QFrame):
    def __init__(self, model : TaskModel):
        super().__init__()
        self.model = model
        self.model.attach(self)

        self.order_btn_icon_name: list[str] = ["fa5s.sort-amount-down", "fa5s.sort-amount-up"]
        self.is_reverse = False

        self._setup_ui()
        self._setup_layout()
        self.refresh_data()

    def _setup_ui(self) -> None:
        # Back Button
        self.back_btn = QPushButton()
        self.back_btn.setIcon(qta.icon("fa5s.chevron-left"))
        self.back_btn.setIconSize(BACK_ICON_SIZE)
        self.back_btn.setFixedWidth(BACK_BTN_WIDTH)
        self.back_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.back_btn.setProperty("class", "hist_back_btn")
        
        # Input
        self.input =  QLineEdit()
        self.input.setFixedSize(INPUT_SIZE)
        self.input.setProperty("class", "hist_input")

        # Order filter
        self.order_btn = QPushButton() 
        self.order_btn.setIcon(qta.icon("fa5s.sort-amount-down")) # Amount-down as default icon
        self.order_btn.setIconSize(BTN_ICON_SIZE)
        self.order_btn.setFixedWidth(BTN_WIDTH)
        self.order_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.order_btn.setProperty("class", "order_btn")
        
        # Month Filter
        self.month_check = QCheckBox()
        self.month_check.setProperty("class", "hist_check")
        self.month_combo = QComboBox()
        self.month_combo.setDisabled(True)
        self.month_combo.addItems([
            "January", "February", "March", "April", "May", "June", 
            "July", "August", "September", "October", "November", "December"
        ])
        self.month_combo.setProperty("class", "hist_combo")

        # Week Day Filter
        self.week_day_check = QCheckBox()
        self.week_day_check.setProperty("class", "hist_check")
        self.week_day_combo = QComboBox()
        self.week_day_combo.setDisabled(True)
        self.week_day_combo.addItems([
            "Monday", "Tuesday", "Wednsday", "Thursday", "Friday", "Saturday", "Sunday"
        ])
        self.week_day_combo.setProperty("class", "hist_combo")

        # Day Filter
        self.spec_day_check = QCheckBox()
        self.spec_day_check.setProperty("class", "hist_check")
        self.spec_day_edit = QDateEdit() 
        self.spec_day_edit.setCalendarPopup(True) 
        self.spec_day_edit.setDate(QDate.currentDate()) 
        self.spec_day_edit.setDisabled(True)
        self.spec_day_edit.setProperty("class", "spec_day_edit")

        # Header Frame
        self.header_frame = QFrame()
        self.header_frame.setFixedHeight(HEADER_HEIGHT)
        self.header_frame.setProperty("class", "hist_header_frame")

        # Task List
        self.task_list = TaskList()
        self.task_list.inner_layout.setContentsMargins(TASK_LIST_MARGINS)
        self.task_list.inner_layout.setSpacing(TASK_LIST_SPACING)
        self.task_list.inner_widget.setProperty("class", "task_list_widget")
        self.task_list.setProperty("class", "hist_task_list_scroll")

        # Global Frame
        self.main_frame = QFrame()
        self.main_frame.setProperty("class", "history_view_frame")

    def _setup_layout(self) -> None:
        input_order_layout = QHBoxLayout()
        input_order_layout.addWidget(self.back_btn)
        input_order_layout.addWidget(self.input)
        input_order_layout.addWidget(self.order_btn)
        
        check_combo_layout = QHBoxLayout()
        check_combo_layout.addWidget(self.month_check)
        check_combo_layout.addWidget(self.month_combo)
        check_combo_layout.addSpacing(CC_SPACING)

        check_combo_layout.addWidget(self.week_day_check)
        check_combo_layout.addWidget(self.week_day_combo)
        check_combo_layout.addSpacing(CC_SPACING)

        check_combo_layout.addWidget(self.spec_day_check)
        check_combo_layout.addWidget(self.spec_day_edit)

        header_layout = QGridLayout()
        header_layout.setContentsMargins(HEADER_MARGINS)
        header_layout.addLayout(input_order_layout, 0, 0, alignment=Qt.AlignmentFlag.AlignLeft)
        header_layout.addLayout(check_combo_layout, 0, 1, alignment=Qt.AlignmentFlag.AlignRight)

        self.header_frame.setLayout(header_layout)

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(MAIN_MARGINS)
        main_layout.addWidget(self.header_frame)
        main_layout.addWidget(self.task_list)
        self.main_frame.setLayout(main_layout)

        # Window Layout
        window_layout = QVBoxLayout()
        window_layout.setContentsMargins(HISTORY_MARGINS)
        window_layout.addWidget(self.main_frame)

        self.setLayout(window_layout)
    
    def bind_btn_clicked(self, btn : QPushButton, action: Callable) -> None:
        btn.clicked.connect(action)
    
    def bind_check_clicked(self, checkBox : QCheckBox, action : Callable):
        checkBox.clicked.connect(action)

    def bind_combo_changed(self, comboBox : QComboBox, action : Callable):
        comboBox.currentIndexChanged.connect(action)

    def bind_dateEdit_changed(self, action : Callable):
        self.spec_day_edit.dateChanged.connect(action)

    def refresh_data(self) -> None:
        month = None
        wd = None
        day = None
        
        if self.month_check.isChecked():
            month = self.month_combo.currentIndex() + 1
            
        if self.week_day_check.isChecked():
            wd = self.week_day_combo.currentIndex() + 1
            
        if self.spec_day_check.isChecked():
            day = self.spec_day_edit.date().toString(format=Qt.DateFormat.ISODate)

        raw_history_list = self.model.get_tasks(month=month, weekday=wd, day_str=day)

        if self.is_reverse: raw_history_list.reverse()

        history_list = [HistoryItem(task["name"], task["date"], task["id"]) for task in raw_history_list]
        self.task_list.load_list(history_list)
   
    

