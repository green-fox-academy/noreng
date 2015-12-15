class Player:
    def __init__(self):
        self.name = ''

    def ask_player_name(self):
        self.name = self.ask_player('Tell me your name: ')

    def ask_player(self, text):
        return input(text)

    def display_name(self):
        print('Hi ' + self.name + '!')
