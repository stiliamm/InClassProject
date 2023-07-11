from datetime import date, timedelta
from item_status import ItemStatus


def add_days_to_now(d):
    return date.today() + timedelta(days=d)


class BoardItem:
    
    def __init__(self, title: str, due_date: int):
        self.title = title
        if self.title == '':
            raise ValueError('Tile must NOT be empty!')
        self.due_date = add_days_to_now(due_date)
        self.status = ItemStatus.OPEN

    
    def revert_status(self):
        start_position = self.status
        previous_postition = ItemStatus.previous(start_position)
        self.status = previous_postition
        return self.status
        
    
    def advance_status(self):
        start_postiton = self.status
        next_position = ItemStatus.next(start_postiton)
        self.status = next_position
        return self.status
       
    
    def info(self):
        return f'{self.title}, [{self.status} | {self.due_date}]'



    