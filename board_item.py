from item_status import ItemStatus
from datetime import date
from event_log import EventLog


class BoardItem:
    
    def __init__(self, title: str, due_date: date):
        self._title = title
        self._due_date = due_date
        self._status = ItemStatus.OPEN
        self._event_logs = []
        self._add_event_log(f"Item created: {self.info()}")

    #================== property methods =======================
    
    @property
    def status(self):
        return self._status
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value: str):
        if len(value) < 5 or len(value) > 30:
            raise ValueError('Title must have more that 5 characters and less that 30.')
        else:
            previous_title = self._title
            self._title = value
            self._add_event_log(f"Title changed from {previous_title} to {value}")
            print('Ok')
    
    @property
    def due_date(self):
        return self._due_date
    
    @due_date.setter
    def due_date(self, value: date):
        if value < date.today():
            raise ValueError('Due date cant be in the past.')

        previous_due_date = self._due_date
        self._due_date = value
        self._add_event_log(f"DueDate changed from {previous_due_date} to {value}")

    #============================ instance methods ================
    
    def revert_status(self):
        previous_status = self._status
        
        if previous_status == ItemStatus.OPEN:
            self._add_event_log(f"Can't change status, already at {previous_status}")
        else:
            self._status = ItemStatus.previous(self._status)
            self._add_event_log(f"Status changed from {previous_status} to {self._status}")


    def advance_status(self):
        previous_status = self._status
        
        if previous_status == ItemStatus.VERIFIED:
            self._add_event_log(f"Can't change status, already at {previous_status}")
        else:
            self._status = ItemStatus.next(self._status)
            self._add_event_log(f"Status changed from {previous_status} to {self._status}")
        
    
    def info(self):
        return f'{self._title}, [{self._status} | {self._due_date}]'
    

    def history(self):
        return '\n'.join(log.info() for log in self._event_logs)

    
    def _add_event_log(self, description: str):
        log = EventLog(description)
        self._event_logs.append(log)
    