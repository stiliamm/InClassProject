class ItemStatus:
    
    # define class attributes
    OPEN = 'Open'
    TODO = 'Todo'
    IN_PROGRESS = 'In progress'
    DONE = 'Done'
    VERIFIED = 'Verified'
    STATUSES = (OPEN, TODO, IN_PROGRESS, DONE, VERIFIED)

    @classmethod
    def next(cls, current):
        try:
            current_index = cls.STATUSES.index(current)
            next_index = current_index + 1
            return cls.STATUSES[next_index]
        except IndexError:
            return cls.STATUSES[-1]

    @classmethod
    def previous(cls, current):
        try:
            current_index = cls.STATUSES.index(current)
            previous_index = current_index - 1
            return cls.STATUSES[previous_index]
        except IndexError:
            return cls.STATUSES[-1]

    