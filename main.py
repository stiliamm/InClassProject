from board_item import BoardItem
from board import Board


def main():
    item = BoardItem("Making files on the database", 2)
    second_item = BoardItem('Encrypt user data', 10)

    item.advance_status()

    board = Board()
    board.items.append(item)
    board.items.append(second_item)

    for board_item in board.items:
        board_item.advance_status()

    for board_item in board.items:
        print(board_item.info())

if __name__ == "__main__":
    main()

