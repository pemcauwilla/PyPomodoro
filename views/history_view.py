import qtawesome as qta
from PyQt6.QtCore import Qt, QMargins, QSize
from PyQt6.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QLineEdit,
    QPushButton,
    QCheckBox,
    QLabel,
    QComboBox
)

# ---- Constants -----
# Window Spacings
HISTORY_MARGINS: QMargins = QMargins(30,30,30,30,)

# Main Layout Spacings
MAIN_MARGINS: QMargins = QMargins(0,0,0,0)

# Header Spacings
HEADER_MARGINS: QMargins = QMargins(15,5,15,0)
HEADER_HEIGHT: int = 70

# Header Measures
INPUT_SIZE: QSize  = QSize(350, 32)

# Button Measures
BTN_ICON_SIZE: QSize = QSize(18,18)

BTN_WIDTH: int = 50

# --------------------

class HistoryView(QFrame):
    def __init__(self):
        super().__init__()
        self._setup_ui()
        self._setup_layout()

    def _setup_ui(self) -> None:
        self.input =  QLineEdit()
        self.input.setFixedSize(INPUT_SIZE)
        self.input.setProperty("class", "hist_input")

        arr = ["fa5s.sort-amount-up", "fa5s.sort-amount-down"]
        self.order_btn = QPushButton()
        self.order_btn.setIcon(qta.icon("fa5s.sort-amount-down"))
        self.order_btn.setIconSize(BTN_ICON_SIZE)
        self.order_btn.setFixedWidth(BTN_WIDTH)

        self.order_btn.setProperty("class", "order_btn")
        
        self.month_check = QCheckBox()
        #self.month_check.setProperty("class", "month_check")
        
        self.month_combo = QComboBox()
        self.month_combo.setProperty("class", "hist_comhist_bo")

        self.week_day_check = QCheckBox()
        
        self.week_day_combo = QComboBox()
        self.week_day_combo.setProperty("class", "hist_combo")

        self.spec_day_check = QCheckBox()
        
        self.spec_day_btn = QPushButton("x")

        self.header_frame = QFrame()
        self.header_frame.setFixedHeight(HEADER_HEIGHT)
        self.header_frame.setProperty("class", "hist_header_frame")

        self.main_frame = QFrame()
        self.main_frame.setProperty("class", "history_view_frame")

    def _setup_layout(self) -> None:
        input_order_layout = QHBoxLayout()
        input_order_layout.addWidget(self.input)
        input_order_layout.addWidget(self.order_btn)
        
        check_combo_layout = QHBoxLayout()
        check_combo_layout.addWidget(self.month_check)
        check_combo_layout.addWidget(self.month_combo)

        check_combo_layout.addWidget(self.week_day_check)
        check_combo_layout.addWidget(self.week_day_combo)

        check_combo_layout.addWidget(self.spec_day_check)
        check_combo_layout.addWidget(self.spec_day_btn)

        header_layout = QGridLayout()
        header_layout.setContentsMargins(HEADER_MARGINS)
        header_layout.addLayout(input_order_layout, 0, 0, alignment=Qt.AlignmentFlag.AlignLeft)
        header_layout.addLayout(check_combo_layout, 0, 1, alignment=Qt.AlignmentFlag.AlignRight)

        self.header_frame.setLayout(header_layout)

        history_layout = QVBoxLayout()
        history_layout.addWidget(QLabel("Teste"))

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        main_layout.setContentsMargins(MAIN_MARGINS)
        main_layout.addWidget(self.header_frame)
        main_layout.addLayout(history_layout)
        self.main_frame.setLayout(main_layout)

        # Window Layout
        window_layout = QVBoxLayout()
        window_layout.setContentsMargins(HISTORY_MARGINS)
        window_layout.addWidget(self.main_frame)

        self.setLayout(window_layout)