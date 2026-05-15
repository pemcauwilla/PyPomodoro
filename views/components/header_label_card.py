from PyQt6.QtCore import Qt, QPointF
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QGraphicsDropShadowEffect,
)

from assets.style_manager import AppColors

class HeaderLabelCard(QFrame):
    def __init__(self, label_txt : str):
        super().__init__()
        self.label_txt = label_txt

        self._setup_ui()
        self._setup_layout()

    def _setup_ui(self):
        self.setProperty("class", "header_label_card")        
        self.setFixedHeight(50)

        shadow = QGraphicsDropShadowEffect()
        shadow.setOffset(QPointF(-2,2))
        shadow.setBlurRadius(15)
        shadow.setColor(QColor(AppColors.THIRD_BG_COLOR))
        self.setGraphicsEffect(shadow)

        self.label = QLabel(self.label_txt)
        self.label.setObjectName("header_card_label")

    def _setup_layout(self):
        main_layout = QHBoxLayout()
        main_layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.setLayout(main_layout)