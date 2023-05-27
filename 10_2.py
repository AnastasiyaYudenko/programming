class Girls:
    def __init__(self, age, name, education, favorites):
        self.age = age
        self.name = name
        self.status_of_education = education
        self.list_of_favorite_things = favorites

    def add_favorites(self, favorite: str):
        self.list_of_favorite_things.append(favorite)


I = Girls(19, 'Nastya', 'student', ['books', 'languages', 'aerial gymnastics'])
Anya = Girls(18, 'Anya', 'pupil', ['music', 'leopard print', 'cars'])
Natasha = Girls(24, 'Natasha', 'teacher', ['tea', 'sport', 'Kyplinov'])
print(Natasha.list_of_favorite_things)