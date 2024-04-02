#задача1 
def calculate(a, b, c):
    result = a * b + c
    return result

def print_result(result):
    print("Результат вычислений: ", result)
n = 5
y = 10
p = 2

calc_result = calculate(x, y, z)
print_result(calc_result)

if calc_result > 20:
    print("Результат больше 20")
else:
    print("Результат меньше или равен 20")
#задача2
def calculate_area(length, width):
    area = dlina * shirina
    return area
def calculate_perimeter(dlina, shirina):
    perimeter = 2 * (dlina + shirina)
    return perimeter
def print_rectangle_properties(area, perimeter):
    print("Площадь прямоугольника:", area)
    print("Периметр прямоугольника:", perimeter)
length = 5
width = 10
rectangle_a = calculate_area(length, width)
rectangle_p = calculate_perimeter(length, width)
print_r(rectangle_area, rectangle_perimeter)
if rectangle_a > 30:
    print("Площадь прямоугольника больше 30")
else:
    print("Площадь прямоугольника меньше или равна 30")
#задача3
def ask_riddles():
    riddles = [
        {"question": "что можно увидеть с закрытыми глазами ", "answer": "сон", "key": "ключ1"},
        {"question": "раскалённая стрела дуб свалила у села", "answer": "молния", "key": "ключ2"},
        {"question": "на дворе горой, а в избе водой: это - ...", "answer": "снег", "key": "ключ3"}
    ]
    attempts = 5
    for riddle in riddles:
        print(riddle["question"])
        for _ in range(attempts):
            user_an = input("Введите ваш ответ: ").lower()
            
            if user_an == riddle["answer"]:
                print("Правильно! Ключ:", riddle["key"])
                break
            else:
                print("Неправильно. Попробуйте еще раз.")
        else:
            print("У вас закончились попытки. Правильный ответ:", riddle["answer"])
ask_riddles()
#задача4
