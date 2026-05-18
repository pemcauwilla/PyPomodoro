from views.components.task_list_item import TaskListItem

class TaskItemController():
    def __init__(self, item_view : TaskListItem, model):
        self.item_view = item_view
        self.model = model

    def _connect_view_signals(self) -> None:
        pass

 
