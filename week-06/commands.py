class Result:
    def __init__(self, success, text = None):
        self.success = success
        self.text = text

    def __repr__(self):
        if self.success == None:
            return 'Not yet implemented'
        return self.text
