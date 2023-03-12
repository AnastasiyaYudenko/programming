import time
from datetime import datetime

t = time.time()
a = int(input("Введите 3х значное число:"))
time.sleep(5)
b = int(input("Введите 4х значное число:"))
if a + b < 10000:
    print("Goood")
else:
    print("Oh noo")
time_lasts = time.time()-t
file_name = 'times_{}.txt'.format(datetime.now().strftime("%d%m%Y_%H%M%S"))
with open(file_name, 'w') as a:
    a.write(str(time_lasts))


