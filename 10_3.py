class Figure:
    def __init__(self, color, size, material):
        self.color = color
        self.size = size
        self.material = material


class Ring(Figure):
    def __init__(self, color, size, material):
        super().__init__(color, size, material)
        self.type = 'Ring'


class Cone(Figure):
    def __init__(self, color, size, material):
        super().__init__(color, size, material)
        self.type = 'Cone'


class Sphere(Figure):
    def __init__(self, color, size, material):
        super().__init__(color, size, material)
        self.type = 'Sphere'


class Box:
    def __init__(self, content: list):
        self.content = content

    def add_to_the_box(self, item):
        self.content.append(item)

    def show_content(self):
        result = 'inside: '
        for item in self.content:
            description = item.size + ' ' + item.color + ' ' + item.type.lower()
            result += description + ' '
        return result


My_Ring = Ring('golden', 'big', 'gold')
print(My_Ring.type)
My_Cone = Cone('red', 'average', 'iron')
print(My_Cone.type)
My_Box = Box([])
My_Box.add_to_the_box(My_Ring)
My_Box.add_to_the_box(My_Cone)
print(My_Box.show_content())
