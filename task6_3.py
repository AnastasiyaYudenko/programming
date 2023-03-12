import time

now = time.time()
a = str(input("Введите полную дату своего рождения: "))
date = time.mktime(time.strptime(a, "%d.%m.%Y"))
b = int((now - date)/86400) #в дне секунд
print("Вы прожили дней: ", b)

