from board_item import BoardItem
from board import Board
from datetime import date, timedelta
from event_log import EventLog
from task import Task
from issues import Issue


def add_days_to_now(d):
    if d < 0:
        raise ValueError('Date should not be in the past')
    return date.today() + timedelta(days=d)


def main():
    task = Task('Test the application flow', 'Steven', add_days_to_now(2))
    task.advance_status()
    task.advance_status()
    task.assignee = 'Not Steven'
    print(task.history())

    # issue = Issue('App flow tests?', 'We need to test the flow!', add_days_to_now(1))
    # issue.advance_status()
    # issue.due_date += timedelta(days=1)
    # print(issue.history())

    # issue = Issue('App flow tests?', 'We need to test the flow!', add_days_to_now(1))
    # task = Task('Dont refactor anything', 'Pesho', add_days_to_now(2))
    #
    # for board_item in [issue, task]:
    #     print(board_item.info())  # prints info like either an issue, or a task


if __name__ == "__main__":
    main()
