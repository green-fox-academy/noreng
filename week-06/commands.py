class Result:
    def __init__(self, success, text = None):
        self.success = success
        self.text = text

    def __repr__(self):
        return self.text
