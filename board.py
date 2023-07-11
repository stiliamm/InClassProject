from board_item import BoardItem

class Board:

    def __init__(self) -> None:
        self._items: list[BoardItem] = []

    
    def add_item(self, item: BoardItem) -> None:
        if item not in self._items:
            self._items.append(item)
        else:
            raise ValueError('Item already in the list')

    
    def count(self) -> int:
        counter = 0
        for _ in self._items:
            counter += 1
        
        return counter