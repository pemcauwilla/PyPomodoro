from datetime import date

from views.pomodoro_view import PomodoroView
from views.add_task_dialog import AddTaskDialog
from models.task_model import TaskModel

class PomodoroController():
    def __init__(self, view : PomodoroView, model : TaskModel):
        self.view = view
        self.model = model

        self._connect_signals()

    def _connect_signals(self) -> None:
        self.view.bind_btn_clicked(btn=self.view.task_list_btn, action=self._task_list_btn_action)
        self.view.bind_btn_clicked(btn=self.view.add_task_btn, action=self._add_btn_action)

        self.view.task_del_sig.connect(self._del_btn_action)

    def _task_list_btn_action(self) -> None:
        current = self.view.task_stacked_wdg.currentIndex()
        self.view.task_stacked_wdg.setCurrentIndex((current + 1) % 2)        
    
    def _add_btn_action(self) -> None: 
        # Visual Changes
        dialog = AddTaskDialog()
        if dialog.exec():
            # Model Changes
            name, duration = dialog.get_add_dialog_values()
            current_date = date.today().strftime("%Y-%m-%d")
            self.model.add_task(name=name, date=current_date, duration=duration)

    def _del_btn_action(self, task_id : int) -> None:
        self.model.delete_task(task_id=task_id)
            

    

