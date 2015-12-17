class MenuItem:
    def __init__(self, id, text, action = None, extra_arg = None):
        self.id = id
        self.text = text
        self.action = action
        self.extra_arg = extra_arg

    def __repr__(self):
        return '{} > {}'.format(self.id, self.text)

class Menu:
    def __init__(self, items):
        self.items = items

    def display(self):
        print(self.get_menu())

    def get_menu(self):
        return "\n".join(str(item) for item in self.items)

    def select_item(self, choice, game):
        for item in self.items:
            if item.id == choice:
                game.prev_action = game.action
                return game.set_next_action(item.action, item.extra_arg)
        return game.set_error("'{}' is wrong input".format(choice))
