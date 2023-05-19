class BankAccount:
    def __init__(self, name, number, balance, password):
        self.owners_name = name
        self.account_number = number
        self.__balance = balance
        self.__password = password

    def change_balance(self, value):
        password = input('Please, enter your password: ')
        if password == self.__password:
            self.__balance = value
            print('balance changed to ' + str(value))
        else:
            print('wrong password!')

    def show_balance(self):
        print(self.__balance)


my_BankAccount = BankAccount('Nastya', 10001110044, 5000, 'chikatoday')
my_BankAccount.change_balance(9500)
my_BankAccount.show_balance()
