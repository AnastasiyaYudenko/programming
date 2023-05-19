class Figure:
    def __init__(self):
        self.color = 'white'

    def change_color(self, new_color):
        self.color = new_color

    def info(self):
        print(self.color)


class Oval(Figure):
    def __init__(self):
        super().__init__()
        self.name = 'oval'

    def info(self):
        print(self.color, self.name)


class Square(Figure):
    def __init__(self):
        super().__init__()
        self.name = 'square'

    def info(self):
        print(self.color, self.name)


my_square = Square()
my_square.info()