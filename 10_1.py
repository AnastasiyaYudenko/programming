class Place:
    def __init__(self, child, activity, name, description):
        self.child = child
        self.activity_now = activity
        self.name = name
        self.description = description

    def check_child(self):
        print(self.child.name, self.child.description)

    def child_make_angry(self):
        self.child.is_angry = True


class Child:
    def __init__(self, description, name):
        self.description = description
        self.name = name
        self.is_angry = False


small_child = Child('the most stupid boy', 'Nikita')
shop = Place(small_child, 'wants_candy', 'shop', 'aaaaaa')
shop.child_make_angry()
print(small_child.is_angry)