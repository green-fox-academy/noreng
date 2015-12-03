class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def __repr__(self):
        status = "[ ]"
        if self.completed:
            status = "[x]"
        return '{} {}'.format(status, self.description)

    def set_completed(self, status):
        self.completed = status
