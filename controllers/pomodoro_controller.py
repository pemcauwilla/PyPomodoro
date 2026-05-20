from datetime import date
import math

from PyQt6.QtCore import QTimer

from views.pomodoro_view import PomodoroView
from views.add_task_dialog import AddTaskDialog
from models.task_model import TaskModel

class PomodoroController():
    def __init__(self, view : PomodoroView, model : TaskModel):
        self.view = view
        self.model = model
        self.timer = QTimer()
        self.timer.setInterval(1000)
       
        self.current_task_id = None
        self.time_left_seconds = 0
        self.is_running = False
        self.current_state = "WORK"
        self.pomodoros_completed = 0

        self.WORK_DURATION = 25 * 60 
        self.SHORT_BREAK = 5 * 60
        self.LONG_BREAK = 15 * 60

        self._connect_signals()

    def _connect_signals(self) -> None:
        self.view.bind_btn_clicked(btn=self.view.task_list_btn, action=self._task_list_btn_action)
        self.view.bind_btn_clicked(btn=self.view.add_task_btn, action=self._add_btn_action)

        self.view.task_del_sig.connect(self._del_btn_action)
        self.view.task_select_sig.connect(self._sel_btn_action)

        self.timer.timeout.connect(self._on_timer_tick)
        self.view.bind_btn_clicked(btn=self.view.start_pause_btn, action=self._toggle_timer_action)

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

    def _sel_btn_action(self, task_id : int) -> None:
        task = self.model.get_task_by_id(task_id)
        # Logic Changes
        self.current_task_id = task["id"]
        self.WORK_DURATION = task["duration"] * 60
        
        self.time_left_seconds = 25 * 60 
        self.current_state = "WORK"
        self.pomodoros_completed = 0
        self.view.start_pause_btn.setDisabled(False) 
        self.view.start_pause_btn.setText("Start")

        self.view.update_header_cards(self.current_state)

        self.view.current_task_lbl.setText(task["name"])
        total_pomodoros = math.ceil(task['duration'] / 25)
        self.view.current_task_status_lbl.setText(f"0/{total_pomodoros}")
        self._update_timer_display()
        
    def _on_timer_tick(self) -> None:
        if self.time_left_seconds > 0:
            self.time_left_seconds -= 1
            self._update_timer_display()
        else:
            self.timer.stop()
            self.is_running = False
            self._handle_timer_completion()
            
    def _toggle_timer_action(self) -> None:
        if self.current_task_id is None:
            return 

        if self.is_running:
            self.timer.stop()
            self.is_running = False
            self.view.start_pause_btn.setText("Start")
        else:
            self.timer.start()
            self.is_running = True
            self.view.start_pause_btn.setText("Pause")

    def _update_timer_display(self) -> None:
        minutes = self.time_left_seconds // 60
        seconds = self.time_left_seconds % 60
        time_str = f"{minutes:02d}:{seconds:02d}"
        self.view.pomodoro_timer_lbl.setText(time_str)    
    
    def _handle_timer_completion(self) -> None:
        total_pomodoros = math.ceil(self.WORK_DURATION / 60 / 25)

        match self.current_state:
            case "WORK":
                self.pomodoros_completed += 1
                
                if self.pomodoros_completed >= total_pomodoros:
                    self.current_state = "INIT" 
                    self.time_left_seconds = 0
                    self.view.start_pause_btn.setText("Terminé !")
                    self.view.start_pause_btn.setDisabled(True) 

                elif self.pomodoros_completed % 4 == 0:
                    self.current_state = "LONG_BREAK"
                    self.time_left_seconds = self.LONG_BREAK 

                else:
                    self.current_state = "SHORT_BREAK"
                    self.time_left_seconds = self.SHORT_BREAK 

            case "SHORT_BREAK" | "LONG_BREAK":
                self.current_state = "WORK"
                self.time_left_seconds = 25 * 60
                
            case "INIT":
                self.timer.stop()
                self.pomodoros_completed = 0
                self.time_left_seconds = 25 * 60
                self.current_state = "WORK"
        
        if self.current_state != "INIT":
            self.timer.start()
            self.is_running = True
            self.view.start_pause_btn.setText("Pause")

        self._update_timer_display()
        self.view.current_task_status_lbl.setText(f"{self.pomodoros_completed}/{total_pomodoros}")
        self.view.update_header_cards(self.current_state)
                

    

