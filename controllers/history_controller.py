from PyQt6.QtWidgets import QWidget
import qtawesome as qta

from views.history_view import HistoryView 
from models.task_model import TaskModel

class HistoryController():
    def __init__(self, view : HistoryView, model : TaskModel):
        self.view = view
        self.model = model

        self._connect_signals()

    def _connect_signals(self) -> None:
        self.view.bind_btn_clicked(btn=self.view.order_btn, action=self._order_btn_action)

        self.view.bind_check_clicked(checkBox=self.view.month_check, action=self._toggle_month_filter)
        self.view.bind_check_clicked(checkBox=self.view.week_day_check, action=self._toggle_weekday_filter)
        self.view.bind_check_clicked(checkBox=self.view.spec_day_check, action=self._toggle_spec_day_filter)
        
        self.view.bind_combo_changed(comboBox=self.view.month_combo, action=self.view.refresh_data)
        self.view.bind_combo_changed(comboBox=self.view.week_day_combo, action=self.view.refresh_data)
        self.view.bind_dateEdit_changed(action=self.view.refresh_data)

    def _order_btn_action(self) -> None:
        self.view.is_reverse = not self.view.is_reverse
        _order_btn_idx = 0 if not self.view.is_reverse else 1
        self.view.order_btn.setIcon(qta.icon(self.view.order_btn_icon_name[_order_btn_idx]))
        self.view.refresh_data()

    def _toggle_month_filter(self) -> None:
        self._enable_filter(self.view.month_combo)
        self.view.refresh_data()

    def _toggle_weekday_filter(self) -> None:
        self._enable_filter(self.view.week_day_combo)
        self.view.refresh_data()

    def _toggle_spec_day_filter(self) -> None:
        self._enable_filter(self.view.spec_day_edit)
        self.view.refresh_data()

    def _enable_filter(self, wid : QWidget) -> None:
        wid.setDisabled(wid.isEnabled())

    



    
        
    

