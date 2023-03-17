import time
import sys

nmb = int(input("Введите любое число:"))
while nmb > 0:
    time.sleep(nmb)
    nmb = int(input("Введите другое число:"))
else:
    sys.exit()



