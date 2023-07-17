from board_item import BoardItem
from datetime import date
from item_status import ItemStatus


class Task(BoardItem):
    def __init__(self, title: str, assignee: str, due_date: date):
        super().__init__(title, due_date)
        self._assignee = assignee
        self.status = ItemStatus.TODO
        self.add_event_log(self.info())

    @property
    def assignee(self):
        return self._assignee

    @assignee.setter
    def assignee(self, value):
        if not (5 <= len(value) <= 30) or value == '':
            raise ValueError('Assignee cannot be empty or have invalid number of chars!')
        old = self._assignee
        self._assignee = value
        self.add_event_log(f'Assignee changed from {old} to {self.assignee}')

    def info(self):
        board_item_info = super().info()
        return f'Task (assigned to: {self.assignee}) {board_item_info}'
