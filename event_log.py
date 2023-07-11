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
        return self._description
    
    def info(self):
        timestamp_str = self._timestamp.strftime("%m/%d/%Y, %H:%M:%S")
        return f'[{timestamp_str}] {self._description}'
