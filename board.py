from board_item import BoardItem


class Board:

    def __init__(self) -> None:
        self._items: list[BoardItem] = []

    def add_item(self, item: BoardItem) -> None:
        if item not in self._items:
            self._items.append(item)
        else:
            raise ValueError('Item already in the list')

    @property
    def items(self):
        return tuple(self._items)

    @property
    def count(self) -> int:
        return len(self._items)
