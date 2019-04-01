from math import *
import matplotlib.pyplot as plt
x1 = int(input("Enter x1 "))
y1 = int(input("Enter y1 "))
x2 = int(input("Enter x2 "))
y2 = int(input("Enter y2 "))
x3 = int(input("Enter x3 "))
y3 = int(input("Enter y3 "))
x = [x1, x2, x3 , x1]
y = [y1, y2, y3 , y1]

leight1 = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
leight2 = sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
leight3 = sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
p = leight1 + leight2 + leight3
pp = p / 2
s = sqrt(pp * (pp - leight1) * (pp - leight2) * (pp - leight3))
plt.plot(x, y)
plt.plot([min(x), max(x)], [0, 0])
plt.plot([0, 0], [min(y), max(y)])
plt.show()
print(leight1)
print(leight2)
print(leight3)
print(p)
print(pp)
print(s)
input("Press enter")