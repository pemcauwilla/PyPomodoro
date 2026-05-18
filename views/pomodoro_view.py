from typing import Callable

from PyQt6.QtCore import Qt, QSize, QMargins
from PyQt6.QtWidgets import (
    QFrame, 
    QLabel,
    QPushButton,
    QVBoxLayout,
    QGridLayout,
    QHBoxLayout,
    QStackedWidget,
    QWidget
)
import qtawesome as qta

from .components.header_label_card import HeaderLabelCard
from .components.task_list import TaskList

# ---- Constants -----
# Buttons 
START_BTN_WIDTH: int = 100

# Header Spacings 
HEADER_SPACING: int = 15
HEADER_MARGIN: QMargins = QMargins(100,0,100,00)

# Current Task Spacings
CRNT_TASK_MARGIN: QMargins = QMargins(10,0,10,0)

# Task Section Spacings
TASK_SEC_SPACING: int = 5
TASK_SEC_MARGINS: QMargins = QMargins(20,10,20,20)

# Task Section Measures
TASK_SEC_WIDTH: int = 350

# Task List Measures
TASK_LIST_WIDTH: int = 240
TASK_LIST_MARGINS: QMargins = QMargins(10,15,10,15)
TASK_LIST_SPACING: int = 10

# Bottom Buttons Spacings
BTM_BTN_SPACING: int = 10
BTM_BTN_MARGINS: QMargins = QMargins(5,5,5,5)

# Bottom Buttons Measures
BTM_FRAME_SIZE: QSize = QSize(130,50)

# Task List + Timer + Buttons Spacings
TTB_MARGINS: QMargins = QMargins(5,0,5,0)

# Header + Timer + Button Spacings
HTB_SPACING: int = 15

# Main Margins
MAIN_MARGINS: QMargins = QMargins(25,20,25,20)
#---------------------

class PomodoroView(QFrame):
    def __init__(self):
        super().__init__()
        self._setup_ui()
        self._setup_layouts()

    def _setup_ui(self) -> None:
        # Header Section
        self.pomodoro_card = HeaderLabelCard("Pomodoro")
        self.pomodoro_card.setObjectName("active_header_btn")
        self.small_break_card = HeaderLabelCard("Small Break")
        self.long_break_card = HeaderLabelCard("Long Break")

        # Timer
        self.pomodoro_timer_lbl = QLabel("25:00")
        self.pomodoro_timer_lbl.setProperty("class", "pom_view_timer")

        self.start_pause_btn = QPushButton("Start")
        self.start_pause_btn.setProperty("class", "pom_view_start_btn") # create two different styles for "each" button
        self.start_pause_btn.setFixedWidth(START_BTN_WIDTH)
        self.start_pause_btn.setCursor(Qt.CursorShape.PointingHandCursor)

        # Task Section
        self.current_task_title_lbl = QLabel("Current Task")
        self.current_task_title_lbl.setProperty("class", "pom_view_current_tsk_title_lbl")

        self.current_task_lbl = QLabel("Study for test")
        self.current_task_lbl.setProperty("class", "pom_view_current_tsk_lbl")

        self.current_task_status_lbl = QLabel("2/3")
        self.current_task_status_lbl.setProperty("class", "pom_view_current_task_lbl") 

        self.task_section_frame = QFrame()
        self.task_section_frame.setFixedWidth(TASK_SEC_WIDTH)
        self.task_section_frame.setProperty("class", "task_section_frame")

        # Current task
        self.current_task_frame = QFrame()
        self.current_task_frame.setProperty("class", "current_task_frame")

        # Buttons Section
        self.add_task_btn = QPushButton()
        self.add_task_btn.setIcon(qta.icon("fa5s.plus"))
        self.add_task_btn.setProperty("class", "pom_view_btn")
        self.add_task_btn.setCursor(Qt.CursorShape.PointingHandCursor)

        self.task_list_btn = QPushButton()
        self.task_list_btn.setIcon(qta.icon("fa5s.list"))
        self.task_list_btn.setProperty("class", "pom_view_btn")
        self.task_list_btn.setCursor(Qt.CursorShape.PointingHandCursor)

        self.task_history_btn = QPushButton()
        self.task_history_btn.setIcon(qta.icon("fa5s.history"))
        self.task_history_btn.setProperty("class", "pom_view_btn")
        self.task_history_btn.setCursor(Qt.CursorShape.PointingHandCursor)

        self.buttons_frame = QFrame()
        self.buttons_frame.setFixedSize(BTM_FRAME_SIZE)
        self.buttons_frame.setProperty("class", "buttons_frame")

        # Task List
        self.task_list = TaskList()
        self.task_list.inner_widget.setProperty("class", "task_list_widget")
        self.task_list.setFixedWidth(TASK_LIST_WIDTH)
        self.task_list.inner_layout.setContentsMargins(TASK_LIST_MARGINS)
        self.task_list.inner_layout.setSpacing(TASK_LIST_SPACING)
        self.task_list.setProperty("class", "task_list_scroll")

        # Task List Stacked Widget + Empty Widget
        self.task_stacked_wdg = QStackedWidget()
        self.task_stacked_wdg.setFixedWidth(TASK_LIST_WIDTH) 
        self.empty_frame = QFrame()
        self.empty_frame.setProperty("class", "empty_frame")

    def _setup_layouts(self) -> None:
        # Header Layout 
        header_layout = QGridLayout()
        header_layout.setSpacing(HEADER_SPACING)
        header_layout.setContentsMargins(HEADER_MARGIN)
        
        header_layout.addWidget(self.pomodoro_card,    0, 1)
        header_layout.addWidget(self.small_break_card, 0, 2)
        header_layout.addWidget(self.long_break_card,  0, 3)
    
        # Task Layout
        crnt_task_layout = QGridLayout()
        crnt_task_layout.setContentsMargins(CRNT_TASK_MARGIN)
        crnt_task_layout.addWidget(self.current_task_lbl,        0, 0, alignment=Qt.AlignmentFlag.AlignLeft)
        crnt_task_layout.addWidget(self.current_task_status_lbl, 0, 0, alignment=Qt.AlignmentFlag.AlignRight)
        self.current_task_frame.setLayout(crnt_task_layout)
        
        # Task Section Layout
        task_section_layout = QVBoxLayout()
        task_section_layout.setSpacing(TASK_SEC_SPACING)
        task_section_layout.setContentsMargins(TASK_SEC_MARGINS)
        task_section_layout.addWidget(self.current_task_title_lbl)
        task_section_layout.addWidget(self.current_task_frame)

        self.task_section_frame.setLayout(task_section_layout)
        
        # Buttons Layout
        buttons_layout = QHBoxLayout()
        buttons_layout.setSpacing(BTM_BTN_SPACING)
        buttons_layout.setContentsMargins(BTM_BTN_MARGINS)
        buttons_layout.addWidget(self.add_task_btn)
        buttons_layout.addWidget(self.task_list_btn)
        buttons_layout.addWidget(self.task_history_btn)

        self.buttons_frame.setLayout(buttons_layout)

        # Task Stacked Widget
        self.task_stacked_wdg.addWidget(self.empty_frame)
        self.task_stacked_wdg.addWidget(self.task_list)
        
        # Header + Timer + Button layout 
        timer_btn_layout = QVBoxLayout()
        timer_btn_layout.setSpacing(HTB_SPACING)
        timer_btn_layout.addWidget(self.pomodoro_timer_lbl,      alignment=Qt.AlignmentFlag.AlignHCenter)
        timer_btn_layout.addWidget(self.start_pause_btn,         alignment=Qt.AlignmentFlag.AlignHCenter)
        timer_btn_layout.addWidget(self.task_section_frame,      alignment=Qt.AlignmentFlag.AlignHCenter)
        timer_btn_layout.addWidget(self.buttons_frame,           alignment=Qt.AlignmentFlag.AlignHCenter)

        # Task_list +  Timer_btn layout
        task_list_timer_btn_layout = QHBoxLayout()
        task_list_timer_btn_layout.setContentsMargins(TTB_MARGINS)
        task_list_timer_btn_layout.addWidget(self.task_stacked_wdg)
        task_list_timer_btn_layout.addLayout(timer_btn_layout)
        task_list_timer_btn_layout.addSpacing(TASK_LIST_WIDTH)
        
        # Main layout
        main_layout = QVBoxLayout()        
        main_layout.setContentsMargins(MAIN_MARGINS)
        main_layout.addLayout(header_layout)
        main_layout.addLayout(task_list_timer_btn_layout)
        
        self.setLayout(main_layout)

    def bind_btn_clicked_action(self, btn : QWidget, action : Callable) -> None:
        btn.clicked.connect(action)

        