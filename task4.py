str = str(input("Чтобы узнать является ли слово палиндромом,введите слово:"))
newstr = ''.join(reversed(str))
if newstr == str:
    print ("Это слово - палиндром")
else:
    print("Это слово не является палиндромом")