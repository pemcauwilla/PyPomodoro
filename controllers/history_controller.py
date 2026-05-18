from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt
import qtawesome as qta

from views.history_view import HistoryView 
from views.components.history_item import HistoryItem
from models.task_model import TaskModel

class HistoryController():
    def __init__(self, view : HistoryView, model : TaskModel):
        self.view = view
        self.model = model

        self._order_btn_icon_name: list[str] = ["fa5s.sort-amount-down", "fa5s.sort-amount-up"]
        self._is_reverse = False

        self._connect_signals()

    def _connect_signals(self) -> None:
        self.view.bind_btn_clicked(btn=self.view.order_btn, action=self._order_btn_action)

        self.view.bind_check_clicked(checkBox=self.view.month_check, action= lambda : self._enable_filter(self.view.month_combo))
        self.view.bind_check_clicked(checkBox=self.view.week_day_check, action= lambda : self._enable_filter(self.view.week_day_combo))
        self.view.bind_check_clicked(checkBox=self.view.spec_day_check, action= lambda : self._enable_filter(self.view.spec_day_edit))
        
        self.view.bind_combo_changed(comboBox=self.view.month_combo, action=self._month_combo_action)
        self.view.bind_combo_changed(comboBox=self.view.week_day_combo, action=self._week_day_combo_action)
        self.view.bind_dateEdit_changed(action=self._day_edit_action)


    def _order_btn_action(self) -> None:
        self._is_reverse = not self._is_reverse
        _order_btn_idx = 0 if not self._is_reverse else 1
        self.view.order_btn.setIcon(qta.icon(self._order_btn_icon_name[_order_btn_idx]))
        self._refresh_history_list()
    
    def _refresh_history_list(self) -> None:
        raw_history_list = self.model.get_all_tasks()
        if self._is_reverse: raw_history_list.reverse()
        
        history_list = [HistoryItem(task["name"], task["date"]) for task in raw_history_list]
        self.view.task_list.load_list(history_list)

    def _enable_filter(self, wid : QWidget) -> None:
        wid.setDisabled(wid.isEnabled())

    def _month_combo_action(self) -> None:
        month = self.view.month_combo.currentIndex() + 1
        raw_history_list = self.model.get_tasks(month=month)

        history_list = [HistoryItem(task["name"], task["date"]) for task in raw_history_list]
        self.view.task_list.load_list(history_list)

    def _week_day_combo_action(self) -> None:
        wd = self.view.week_day_combo.currentIndex() + 1
        raw_history_list = self.model.get_tasks(weekday=wd)

        history_list = [HistoryItem(task["name"], task["date"]) for task in raw_history_list]
        self.view.task_list.load_list(history_list)

    def _day_edit_action(self) -> None:
        day = self.view.spec_day_edit.date().toString(format=Qt.DateFormat.ISODate)
        raw_history_list = self.model.get_tasks(day_str=day)

        history_list = [HistoryItem(task["name"], task["date"]) for task in raw_history_list]
        self.view.task_list.load_list(history_list)
    




    
        
    

