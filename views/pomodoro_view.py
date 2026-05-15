from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QFrame, 
    QLabel,
    QPushButton,
    QVBoxLayout,
    QGridLayout,
    QHBoxLayout
)

class PomodoroView(QFrame):
    def __init__(self):
        super().__init__()
        self._setup_ui()
        self._setup_layouts()

    def _setup_ui(self) -> None:
        # Header Section
        self.pomodoro_lbl = QLabel("Pomodoro")
        self.pomodoro_lbl.setProperty("class", "pom_view_header_lbl")

        self.small_break_lbl = QLabel("Small Break")
        self.small_break_lbl.setProperty("class", "pom_view_header_lbl")

        self.long_break_lbl = QLabel("Long Break")
        self.long_break_lbl.setProperty("class", "pom_view_header_lbl")

        # Timer
        self.pomodoro_timer_lbl = QLabel("25:00")
        self.pomodoro_timer_lbl.setProperty("class", "pom_view_timer")

        self.start_pause_btn = QPushButton("Start")
        self.start_pause_btn.setProperty("class", "pom_view_start_btn") # create two different styles for "each" button

        # Task Section
        self.current_task_title_lbl = QLabel("Current Task")
        self.current_task_title_lbl.setProperty("class", "pom_view_current_tsk_title_lbl")

        self.current_task_lbl = QLabel("Study for test")
        self.current_task_lbl.setProperty("class", "pom_view_current_tsk_lbl")

        self.current_task_status_lbl = QLabel("2/3")
        self.current_task_status_lbl.setProperty("class", "pom_view_current_task_lbl") 

        # Buttons Section
        self.task_list_btn = QPushButton("X")
        self.task_list_btn.setProperty("class", "pom_view_btn")

        self.task_history_btn = QPushButton("Y")
        self.task_history_btn.setProperty("class", "pom_view_btn")

    def _setup_layouts(self) -> None:
        # Main Layout 
        header_layout = QGridLayout()
        header_layout.setSpacing(20)
        header_layout.setContentsMargins(0,0,0,0)
        header_layout.addWidget(self.pomodoro_lbl,    0, 1,  alignment=Qt.AlignmentFlag.AlignHCenter)
        header_layout.addWidget(self.small_break_lbl, 0, 2,  alignment=Qt.AlignmentFlag.AlignHCenter)
        header_layout.addWidget(self.long_break_lbl,  0, 3 , alignment=Qt.AlignmentFlag.AlignHCenter)
    
        header_frame = QFrame()
        header_frame.setLayout(header_layout)
        header_frame.setStyleSheet("background-color:red;")

        # Task Layout
        task_layout = QGridLayout()
        task_layout.addWidget(self.current_task_lbl,        0, 0, alignment=Qt.AlignmentFlag.AlignLeft)
        task_layout.addWidget(self.current_task_status_lbl, 0, 0, alignment=Qt.AlignmentFlag.AlignRight)

        task_frame = QFrame()
        task_frame.setLayout(task_layout)
        task_frame.setStyleSheet("background-color:blue;")

        # Task Section Layout
        task_section_layout = QVBoxLayout()
        task_section_layout.setSpacing(5)
        task_section_layout.setContentsMargins(50,10,50,10)
        task_section_layout.addWidget(self.current_task_title_lbl)
        task_section_layout.addWidget(task_frame)

        task_section_frame = QFrame()
        task_section_frame.setLayout(task_section_layout)
        task_section_frame.setStyleSheet("background-color:pink;")

        # Buttons Layout
        buttons_layout = QHBoxLayout()
        buttons_layout.setSpacing(10)
        buttons_layout.setContentsMargins(5,5,5,5)
        buttons_layout.addWidget(self.task_list_btn)
        buttons_layout.addWidget(self.task_history_btn)

        buttons_frame = QFrame()
        buttons_frame.setLayout(buttons_layout)
        buttons_frame.setStyleSheet("background-color: blue;")

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.setSpacing(10)
        main_layout.setContentsMargins(50,20,50,20)
        main_layout.addWidget(header_frame)
        main_layout.addWidget(self.pomodoro_timer_lbl)
        main_layout.addWidget(self.start_pause_btn)
        main_layout.addWidget(task_section_frame)
        main_layout.addWidget(buttons_frame)

        self.setLayout(main_layout)