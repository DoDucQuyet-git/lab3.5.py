# Bai 5
import math

a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
c = float(input("Nhap c: "))

if a == 0:
    if b != 0:
        print("x =", -c/b)
    else:
        print("Vo nghiem")
else:
    delta = b*b - 4*a*c

    if delta < 0:
        print("Vo nghiem")
    elif delta == 0:
        print("Nghiem kep:", -b/(2*a))
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("x1 =", x1)
        print("x2 =", x2)
