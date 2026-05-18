from views.main_window import MainWindow
from models.task_model import TaskModel
from .history_controller import HistoryController
from .pomodoro_controller import PomodoroController


class MainViewController():
    def __init__(self, view : MainWindow, model : TaskModel):
        self.view = view
        self.model = model

        self.pom_controller = PomodoroController(view=self.view.pom_view, model=self.model)
        self.hist_controller=  HistoryController(view=self.view.hist_view, model=self.model)

        self._connect_signals()

    def _connect_signals(self) -> None:
        self.view.bind_btn_clicked(btn=self.view.pom_view.task_history_btn, action=self._stacked_widget_action)
        self.view.bind_btn_clicked(btn=self.view.hist_view.back_btn, action=self._stacked_widget_action)

    def _stacked_widget_action(self) -> None:
        if self.view.central_widget.currentIndex() == 0:
            self.hist_controller._apply_filters()
        
        self.view.central_widget.setCurrentIndex(1 - self.view.central_widget.currentIndex())

    

        