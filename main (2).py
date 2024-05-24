#Задача 3
def three_aces0(var1=None, var2=None, var3=None):
    args = [var1, var2, var3]
    result = [f"{key} = {value}" for key, value in zip(["var1", "var2", "var3"], args) if value is not None]
    if len(result) > 0:
        print("Переданы аргументы:", ", ".join(result))
    else:
        print("Не передано ни одного аргумента")
        
#Задача 4
from datetime import datetime
from time import sleep

def get_time_now(msg: str, now: str = None):
    global now

    if now is None:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")

    print(f"{msg} {now}")
get_time_now("Сейчас такое время: ")
sleep(1)
get_time_now("Прошла секунда: ")
sleep(1)
get_time_now("Ничего не понимаю... ")

#Задача 5
import inspect

def inspect_function(func):
    signature = inspect.signature(func)

    print(f"Название функции: {func.__name__}")
    print("Список параметров:")

    for parameter in signature.parameters.values():
        print(f" - {parameter.name}:")
        print(f"    Тип аннотации: {parameter.annotation}")
        print(f"    Тип по умолчанию: {parameter.default}")
        print(f"    Позиционный или именованный: {parameter.kind}")

    print()
    
#Задача 1
def sum_stack(start, end):
  if start > end:
    start, end = end, start
  numbers = list(range(start, end + 1))
  total = sum(numbers)
  return total

#Задача 2
def func1():
  param = 4
  def inner():
    param += 1
    return param
  return inner
#Возникнет ошибка NameError: name 'param' is not defined.

def func2():
  param = 4
  def inner(param):
    param += 1
    return param
  inner(param)
  return param
  #Причина: параметр param, переданный в функцию inner, имеет значение 4, и значение param не изменяется внутри функции inner.
  
def func3():
  param = 4
  def inner(param):
    param += 1
    return param
  param = inner(param)
  return param
#Причина: параметр param объявлен в области видимости функции outer и доступен в функции inner. Когда функция inner вызывается с параметром param, значение param (4) увеличивается на 1.










