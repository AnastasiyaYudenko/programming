class Family:
    def __init__(self):
        self.husband = 'husband'
        self._wife = 'wife'
        self.__child = 'child'

    def display(self):
        print(self._wife)
        print(self.__child)


n_1 = Family()
print(n_1.__child)
n_1.display()
