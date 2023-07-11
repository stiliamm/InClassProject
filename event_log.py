from datetime import datetime

class EventLog:
    
    def __init__(self, description: str) -> None:
        self._description = description
        self._timestamp = datetime.now()

    @property
    def timestamp(self):
        return self._timestamp
    
    @property
    def description(self):
        if self._description == '':
            raise ValueError('Cannot be empty!')
        return self._description
    
    def info(self):
        timestamp_str = self.timestamp.strftime("%m/%d/%Y, %H:%M:%S")
        return f'[{timestamp_str}] {self.description}'
