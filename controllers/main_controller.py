from views.main_window import MainWindow
from models.task_model import TaskModel
from .history_controller import HistoryController
from .pomodoro_controller import PomodoroController
from views.components.history_item import HistoryItem

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
            self._refresh_history_list()
        
        self.view.central_widget.setCurrentIndex(1 - self.view.central_widget.currentIndex())

    def _refresh_history_list(self) -> None:
        raw_history_list = self.model.get_all_tasks()
        history_list = [HistoryItem(task["name"], task["date"]) for task in raw_history_list]
        
        self.view.hist_view.task_list.load_list(history_list)

        