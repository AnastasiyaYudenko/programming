
import  matplotlib.pyplot as plt
import numpy as np
# Создайте график вторым способом так, чтобы у вас получился зигзагообразная линия

plt.plot([1, 2, 4], [1, 8, 16])
plt.ylabel('some numbers')
plt.show()

# Постройте любой график с зелёными треугольниками

plt.plot([1.5, 3, 4.5], [1, 2, 3],'g<')
plt.show()

#Создайте вектор длины 10 со случайными значениями и постройте также несколько линий за одну команду
# (используйте функции, отличные от тех, что приведены в примере выше, для построения графиков!)

import random
a = np.array(random.sample(range(1, 100), 10))

plt.plot(a, a-1, 'k', a, a/2, 'c')
plt.show()

#Создайте любой график и подпишите у него заголовок и названия осей:


plt.plot([4, 2, 6, 3], [8, 10, 12, 14], 'c')
plt.xlabel('Summer')
plt.ylabel('Winter')
plt.title('Seasons')
plt.show()

# Изучите код ниже (главным образом строку с функцией plt.annotate()), убедитесь, что вы его понимаете и измените код следующим образом:
# Укажите на локальный минимум (любой) зелёной стрелочкой и текстом "local min".

ax = plt.subplot(111)

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2)

plt.annotate('local min', xy=(1.5, -1), xytext=(3, -1.5),
            arrowprops=dict(facecolor='green', shrink=0.05),
            )

plt.ylim(-2,2)
plt.show()


#Постройте график любой функции (которой ещё не было в примерах), укажите название самого графика и осей,
# подпишите некоторые элементы на графике (выберите любые +- значимые элементы вашей функции):

t = np.arange(0., 16., 1.)

plt.plot(t, np.sqrt(t), 'k')
plt.annotate('main point', xy=(0.95, 1), xytext=(3, 1.5),
            arrowprops=dict(facecolor='red', shrink=0.03),
           )
plt.annotate('main point2', xy=(15, 3.8), xytext=(14, 3),
           arrowprops=dict(facecolor='green', shrink=0.03),
           )
plt.xlabel('Cherry')
plt.ylabel('Raspberry')
plt.title('Berries')

plt.show()

#Постройте несколько линий (можно две) разных цветов на одном графике, отображающих динамику чего-либо.
# Данные можно найти или придумать самим:)


x = np.arange(0.1, 4, 0.1)
y = np.exp(-1.0 * x)
y2 = np.exp(-0.5 * x)
plt.plot(x, y, x, y2, 'm')
plt.xlabel('Время обучения на ФиПЛе')
plt.ylabel('Время сна')
plt.title('Динамика')
plt.show()
