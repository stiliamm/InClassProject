from board_item import BoardItem
from board import Board
from datetime import date, timedelta
from event_log import EventLog


def add_days_to_now(d):
    if d < 0:
        raise ValueError('Date should not be in the past')
    return date.today() + timedelta(days=d)


def main():
    item = BoardItem('Refactor this mess', add_days_to_now(2))
    another_item = BoardItem('Dont refactor anything', add_days_to_now(2))

    board = Board()
    board.add_item(item)
    board.add_item(another_item)
    board.add_item(item)
    board.add_item(item)
    print(board.count())
    
    
    
    # item.due_date += timedelta(days=365 * 2)
    # item.title = 'Not that important'
    # item.revert_status()
    # item.advance_status()
    # item.revert_status()
    # print(item.history())
    

if __name__ == "__main__":
    main()

