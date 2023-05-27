class Table:
    def __init__(self, l, w, h):
        self.long = l
        self.width = w
        self.height = h

    def outing(self):
        print(self.long,self.width,self.height)


class Kitchen(Table):
    def howplaces(self, n):
        if n < 2:
            print("It isn't kitchen table")
        else:
            self.places = n

    def outplaces(self):
        print(self.places)


class Worker(Table):
    def square(self):
        return self.width * self.long

    def perimeter(self):
        return 2 * (self.long + self.width)


t_room1 = Kitchen(2,1,0.5)
t_room1.outing()
t_room1.howplaces(5)
t_room1.outplaces()


t_2 = Table(1,3,0.7)
t_2.outing()


t_3 = Worker(5, 6, 0.8)
t_3.square()
t_3.perimeter()
