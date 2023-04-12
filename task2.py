str_1 = str(input('напишите что-нибудь:'))
symbol = []
repeat_symbol = []
for i in str_1:
    if (i in symbol) and (i not in repeat_symbol):
        repeat_symbol.append(i)
    symbol.append(i)
print(f"В введеной последовательности найдены дубликаты символа: {repeat_symbol}")