from board_item import BoardItem
from datetime import date


class Issue(BoardItem):
    def __init__(self, title: str, description: str, due_date: date):
        super().__init__(title, due_date)
        self.description = description
        self.add_event_log(self.info())

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if value == '':
            self._description = 'No description'
        self._description = value

    def info(self):
        board_item_info = super().info()  # obtain base class information
        return f'Issue ({self._description}) {board_item_info}'

    def log_event(self, description):
        super().add_event_log(description)
