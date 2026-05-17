from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QDialog,
    QLineEdit,
    QLabel,
    QSpinBox,
    QVBoxLayout,
    QDialogButtonBox
)

# Constants
LAYOUT_SPACING = 15
# ---------

class AddTaskDialog(QDialog):
    def __init__(self):
        super().__init__()

        self._setup_ui()
        self._setup_layout()

    def _setup_ui(self) -> None:
        self.setWindowTitle("Add new task")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setObjectName("add_dialog")

        self.title_lbl = QLabel("Enter the task name")
        
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Study MVC architecture...")

        self.time_lbl = QLabel("Enter the task duration")
        
        self.duration = QSpinBox()
        self.duration.setRange(1, 120)     
        self.duration.setValue(25)
        self.duration.setSuffix(" min")

        self.buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        self.buttons.accepted.connect(self.accept) 
        self.buttons.rejected.connect(self.reject)

    def _setup_layout(self) -> None:
        layout = QVBoxLayout(self)
        layout.setSpacing(LAYOUT_SPACING)

        layout.addWidget(self.title_lbl)
        layout.addWidget(self.name_input)
        layout.addWidget(self.time_lbl)
        layout.addWidget(self.duration)
        layout.addWidget(self.buttons, alignment=Qt.AlignmentFlag.AlignCenter)

    def get_add_dialog_values(self) -> tuple[str, int]:
        return self.name_input.text(), self.duration.value()