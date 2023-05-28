class Movie:
    def __init__(self, years, name, spoiler, date, secret_word):
        self.years = years
        self.name = name
        self.__spoiler = spoiler
        self.date_of_creation = date
        self.secret_word = secret_word

    def get_spoiler(self):
        return self.__spoiler

    def movie_birthday(self, today):
        if today == self.date_of_creation:
            self.years += 1
            print('Today is the birthday of this film!')

    def tell_me_one_spoiler(self):
        secret_word = input('say me the secret word and I will tell you one spoiler:  ')
        if secret_word == self.secret_word:
            print('the spoiler is: ' + self.__spoiler)
        else:
            print('No-no_no!')

    def change_spoiler(self, new):
        if type(new) == str and len(new) > 0:
            self.__spoiler = new


my_movie = Movie(19, 'The_Notebook', 'they will break up and she will go to another city', '20.05', 'ilovequotes')
my_movie.movie_birthday('20.05')
print(my_movie.years)
my_movie.tell_me_one_spoiler()
my_movie.change_spoiler('she will merry another men, but cheat on him')
my_movie.tell_me_one_spoiler()
print(my_movie.get_spoiler())