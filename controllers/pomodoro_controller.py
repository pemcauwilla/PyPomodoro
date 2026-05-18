from datetime import date

from views.pomodoro_view import PomodoroView
from views.add_task_dialog import AddTaskDialog
from views.components.task_list_item import TaskListItem
from models.task_model import TaskModel

class PomodoroController():
    def __init__(self, view : PomodoroView, model : TaskModel):
        self.view = view
        self.model = model

        self._connect_signals()

    def _connect_signals(self) -> None:
        self.view.bind_btn_clicked(btn=self.view.task_list_btn, action=self._task_list_btn_action)
        self.view.bind_btn_clicked(btn=self.view.add_task_btn, action=self._add_btn_action)

    def _task_list_btn_action(self) -> None:
        # Visual Changes
        current = self.view.task_stacked_wdg.currentIndex()
        self.view.task_stacked_wdg.setCurrentIndex((current + 1) % 2)        
    
        # Model Changes
        self._refresh_task_list()

    def _add_btn_action(self) -> None: 
        # Visual Changes
        dialog = AddTaskDialog()
        if dialog.exec():
            # Model Changes
            name, duration = dialog.get_add_dialog_values()
            current_date = date.today().strftime("%Y-%m-%d")
            self.model.add_task(name=name, date=current_date, duration=duration)
            self._refresh_task_list()

    # ---------- HELPERS ------------
    def _refresh_task_list(self) -> None:
        raw_task_list = self.model.get_all_tasks()
        task_list = [TaskListItem(task["name"], task["id"]) for task in raw_task_list]
        
        self.view.task_list.load_list(task_list)

