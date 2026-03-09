#!/usr/bin/env python
# coding: utf-8

# Задание 1
try:
    number = float(input("Введите число: "))

    if number < 0:
        raise ValueError

    rub = int(number)
    kop = int(round((number - rub) * 100))

    print(f"{rub} руб. {kop} коп.")

except:
    print("Некорректный формат!")


# Задание 2
spisok = [1, 2, 3, 4, 5]

flag = True

for i in range(len(spisok)-1):
    if spisok[i] >= spisok[i+1]:
        flag = False
        break

print(flag)


# Задание 3
card = input("Введите номер карты: ")

result = card[:4] + " **** **** " + card[-4:]

print(result)


# Задание 4
text = input("Введите текст: ")

words = text.split()

big = []
mid = []
small = []

for w in words:
    if len(w) > 7:
        big.append(w)
    elif 4 <= len(w) <= 7:
        mid.append(w)
    else:
        small.append(w)

print(*big)
print(*mid)
print(*small)


# Задание 5
text = input("Введите предложение: ")

words = text.replace(",", " ,").split()

result = []

for w in words:
    if w[0].isupper():
        result.append(w.upper())
    else:
        result.append(w)

print(" ".join(result).replace(" ,", ","))


# Задание 6
text = input("Введите текст: ")

for s in text:
    if text.count(s) == 1:
        print(s, end="")


# Задание 7
spisok = ["www.google", "yandex.ru", "www.youtube", "github", "www.test.org", "example.com"]

new_spisok = [
    ("http://" + s if s.startswith("www") else s) + ("" if s.endswith(".com") else ".com")
    for s in spisok
]

print(new_spisok)


# Задание 8
import random

n = random.randint(1, 10000)

spisok = [random.randint(1, 100) for i in range(n)]

size = 1
while size < n:
    size *= 2

spisok += [0] * (size - n)

print("n =", n)
print("Размер массива =", len(spisok))


# Задание 9
# Спрашиваем сумму и превращаем её в число (int)
amount = int(input("Введите сумму: "))

# Номинал : Количество штук (словарь)
nominal = {5000: 10, 2000: 10, 1000: 10, 500: 10, 200: 10, 100: 10, 50: 10, 10: 10, 5: 10, 2: 10, 1: 10}

results = [] # Сюда будем складывать строки типа "5*1000"

# Перебираем купюры в словаре
for dengi in nominal.keys():
    if amount >= dengi:
        count = amount // dengi # Сколько купюр этого номинала можем дать

        # Проверяем, есть ли столько купюр в банкомате
        if count > nominal[dengi]:
            count = nominal[dengi]

        if count > 0:
            results.append(f"{count}*{dengi}")
            amount -= count * dengi # Вычитаем выданное из суммы

# Проверяем, удалось ли выдать всю сумму
if amount == 0:
    print(" + ".join(results))
else:
    print("Операция не может быть выполнена!")


# Задание 10
password = input("Введите пароль: ")

score = 0

if len(password) >= 8:
    score += 1

if any(c.isdigit() for c in password):
    score += 1

if any(c.isupper() for c in password):
    score += 1

if any(c in "!@#$%^&*" for c in password):
    score += 1

if score <= 1:
    print("Слабый пароль")
elif score == 2:
    print("Средний пароль")
else:
    print("Надежный пароль")


# Задание 11
def frange(start, stop, step):
    x = start
    while x < stop:
        yield round(x, 2)
        x = round(x + step, 2)

for x in frange(1, 5, 0.1):
    print(x)


# Задание 12
def get_frames(signal, size, overlap):

    step = int(size * (1 - overlap))
    i = 0

    while i + size <= len(signal):
        yield signal[i:i+size]
        i += step

signal = [1,2,3,4,5,6,7,8,9,10]

for frame in get_frames(signal, size=4, overlap=0.5):
    print(frame)


# Задание 13
def extra_enumerate(spisok):

    total = sum(spisok)
    cum = 0

    for i, elem in enumerate(spisok):
        cum += elem
        frac = cum / total
        yield i, elem, cum, frac

x = [1,3,4,2]

for i, elem, cum, frac in extra_enumerate(x):
    print(elem, cum, round(frac,2))


# Задание 14
def non_empty(func):

    def wrapper():
        result = func()
        return [x for x in result if x and x != None]
    return wrapper

@non_empty
def get_pages():
    return ['chapter1', '', 'contents', '', 'line1']

print(get_pages())


# Задание 15
def pre_process(a=0.97):

    def decorator(func):

        def wrapper(s):

            new_s = [s[0]]

            for i in range(1, len(s)):
                value = s[i] - a * s[i-1]
                new_s.append(value)

            func(new_s)

        return wrapper

    return decorator

@pre_process(a=0.93)
def plot_signal(s):
    for sample in s:
        print(sample)

plot_signal([1,2,3,4,5])


# Задание 16
import random
import itertools
from datetime import datetime, timedelta

teams = ["Team1","Team2","Team3","Team4",
         "Team5","Team6","Team7","Team8",
         "Team9","Team10","Team11","Team12",
         "Team13","Team14","Team15","Team16"]
random.shuffle(teams)

groups = [teams[i:i+4] for i in range(0,16,4)]

print("Группы:")

for i, g in enumerate(groups,1):
    print("Группа", i, ":", g)

print("\nИгры:")

start = datetime(datetime.now().year, 9, 14, 22, 45)

games = list(itertools.combinations(teams, 2))

date = start

for t1, t2 in games:
    print(f"{date.strftime('%d/%m/%Y, %H:%M')}  {t1} - {t2}")
    date += timedelta(days=14)
