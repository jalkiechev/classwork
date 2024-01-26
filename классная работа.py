#задача 1 
x = int(input("введите число: "))
y = 7*x+5 
print("Ответ: y=",y)
#Задача 2 
side = int(input("Введите длину стороны квадрата: "))
perimeter = 4 * side
print("Периметр квадрата равен:", perimeter)
#Задача 3
radius = int(input("Введите радиус окружности: "))
circumference = 2 * 3.14159 * radius
print("Длина окружности равна:", circumference)
#Задача 4
radius = int(input("Введите радиус окружности: "))
pi = 3.14159
circumference = 2 * pi * radius
print("Длина окружности равна:", circumference)
#Задача 5 
a = float(input("Введите длину первого катета: "))
b = float(input("Введите длину второго катета: "))
c_squared = a**2 + b**2
c = c_squared ** 0.5
print("Длина гипотенузы равна:", c) 
#Задача 6 
a = float(input("Введите длину первого катета: "))
b = float(input("Введите длину второго катета: "))
c = math.sqrt(a**2 + b**2)
perimeter = a + b + c
print("Периметр треугольника равен:", perimeter)
#Задача 7 
# Ввод сторон треугольника
a = int(input("Введите длину стороны a: "))
b = int(input("Введите длину стороны b: "))
c = int(input("Введите длину стороны c: "))
perimeter = a + b + c
print("Периметр треугольника:", perimeter)
diagonal1 = (a**2 + b**2)
diagonal2 = (b**2 + c**2)
diagonal3 = (a**2 + c**2)
print("Диагонали треугольника:", diagonal1, diagonal2, diagonal3)
#Задача 8 

#Задача 9 
a = float(input("Введите длину ребра куба: "))
surface_area = 6 * a**2
volume = a**3
print("Площадь поверхности куба:", surface_area)
print("Объем куба:", volume)
#Задача 10 
a = int(input("Введите длину меньшего основания трапеции: "))
b = int(input("Введите длину большего основания трапеции: "))
h = int(input("Введите высоту трапеции: "))
c = ((b - a)**2 + h**2)
perimeter = a + b + 2*c
print("Периметр трапеции равен:", perimeter)
















