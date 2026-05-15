from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QFrame, 
    QLabel,
    QPushButton,
    QVBoxLayout,
    QGridLayout,
    QHBoxLayout
)
import qtawesome as qta

from .components.header_label_card import HeaderLabelCard

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
        self.start_pause_btn.setFixedWidth(100)
        self.start_pause_btn.setCursor(Qt.CursorShape.PointingHandCursor)

        # Task Section
        self.current_task_title_lbl = QLabel("Current Task")
        self.current_task_title_lbl.setProperty("class", "pom_view_current_tsk_title_lbl")

        self.current_task_lbl = QLabel("Study for test")
        self.current_task_lbl.setProperty("class", "pom_view_current_tsk_lbl")

        self.current_task_status_lbl = QLabel("2/3")
        self.current_task_status_lbl.setProperty("class", "pom_view_current_task_lbl") 

        # Buttons Section
        self.task_list_btn = QPushButton()
        self.task_list_btn.setIcon(qta.icon("fa5s.list"))
        self.task_list_btn.setProperty("class", "pom_view_btn")
        self.task_list_btn.setCursor(Qt.CursorShape.PointingHandCursor)

        self.task_history_btn = QPushButton()
        self.task_history_btn.setIcon(qta.icon("fa5s.history"))
        self.task_history_btn.setProperty("class", "pom_view_btn")
        self.task_history_btn.setCursor(Qt.CursorShape.PointingHandCursor)

    def _setup_layouts(self) -> None:
        # Header Layout 
        header_layout = QGridLayout()
        header_layout.setSpacing(15)
        header_layout.setContentsMargins(100,0,100,0)
        
        header_layout.addWidget(self.pomodoro_card,    0, 1)
        header_layout.addWidget(self.small_break_card, 0, 2)
        header_layout.addWidget(self.long_break_card,  0, 3)
    
        # Task Layout
        task_layout = QGridLayout()
        task_layout.setContentsMargins(10,0,10,0)
        task_layout.addWidget(self.current_task_lbl,        0, 0, alignment=Qt.AlignmentFlag.AlignLeft)
        task_layout.addWidget(self.current_task_status_lbl, 0, 0, alignment=Qt.AlignmentFlag.AlignRight)

        task_frame = QFrame()
        task_frame.setLayout(task_layout)
        task_frame.setProperty("class", "task_frame")

        # Task Section Layout
        task_section_layout = QVBoxLayout()
        task_section_layout.setSpacing(5)
        task_section_layout.setContentsMargins(20,10,20,10)
        task_section_layout.addWidget(self.current_task_title_lbl)
        task_section_layout.addWidget(task_frame)

        task_section_frame = QFrame()
        task_section_frame.setFixedWidth(350)
        task_section_frame.setLayout(task_section_layout)
        task_section_frame.setProperty("class", "task_section_frame")

        # Buttons Layout
        buttons_layout = QHBoxLayout()
        buttons_layout.setSpacing(10)
        buttons_layout.setContentsMargins(5,5,5,5)
        buttons_layout.addWidget(self.task_list_btn)
        buttons_layout.addWidget(self.task_history_btn)

        buttons_frame = QFrame()
        buttons_frame.setLayout(buttons_layout)
        buttons_frame.setFixedSize(130, 50)
        buttons_frame.setProperty("class", "buttons_frame")

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(50,20,50,20)
        main_layout.addLayout(header_layout)
        main_layout.addWidget(self.pomodoro_timer_lbl, alignment=Qt.AlignmentFlag.AlignHCenter)
        main_layout.addWidget(self.start_pause_btn,    alignment=Qt.AlignmentFlag.AlignHCenter)
        main_layout.addWidget(task_section_frame,      alignment=Qt.AlignmentFlag.AlignHCenter)
        main_layout.addWidget(buttons_frame,           alignment=Qt.AlignmentFlag.AlignHCenter)

        self.setLayout(main_layout)