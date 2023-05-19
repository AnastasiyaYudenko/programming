class Newspaper:
    def __init__(self, page, total):
        self.current_page = page
        self.total_pages = total

    def read(self):
        self.current_page += 1
        self.__how_much()

    def __how_much(self):
        if self.current_page >= 5:
            self.total_pages = 'a bit more!'


me_ns = Newspaper(3, 8)
me_ns.read()
me_ns.read()
me_ns.read()
print(me_ns.current_page, me_ns.total_pages)