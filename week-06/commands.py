class Result:
    def __init__(self, success, text = None):
        self.success = success
        self.text = text

    def __repr__(self):
        return self.text

class Not_Implemented:
    def __init__(self):
        self.success = False
        self.text = 'Not yet implemented'

class Exit:
    def __init__(self):
        self.success  = None
