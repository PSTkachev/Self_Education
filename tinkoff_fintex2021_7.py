"""У Артемия есть бесконечное число монет, каждая из которых одного из трех номиналов.
Его интересует, какие суммы от 1 до N рублей он может набрать в свой кошелек,
если там заранее лежала монета величиной в 1 рубль.

Формат входных данных
Первая строка содержит число N — ограничение на стоимость кошелька (1 ﻿≤﻿ N ﻿≤﻿﻿ 10^{18}).
Вторая строка содержит три числа A, B и C, задающие достоинства типов монет (1 ≤﻿ A, B, C ﻿≤﻿ 100000).

Формат выходных данных
Выведите единственное число — количество сумм, которые можно набрать в кошельке.

Замечание
В первом примере возможны следующие варианты:
1 = 1
1 + 4 = 5
1 + 7 = 8
1 + 4 + 4 = 9
1 + 9 = 10
1 + 4 + 7 = 12
1 + 4 + 4 + 4 = 13
1 + 4 + 9 = 14
1 + 7 + 7 = 15

Примеры данных
Пример 1
15
4 7 9
Лтвет:
9
"""

def func_1(x):
    if x + coin_1 <= N:
        num_of_sum.append(x + coin_1)
        func_1(x + coin_1)
        func_2(x + coin_1)
        func_3(x + coin_1)
def func_2(x):
    if x + coin_2 <= N:
        num_of_sum.append(x + coin_2)
        func_1(x + coin_2)
        func_2(x + coin_2)
        func_3(x + coin_2)

def func_3(x):
    if x + coin_3 <= N:
        num_of_sum.append(x + coin_3)
        func_1(x + coin_3)
        func_2(x + coin_3)
        func_3(x + coin_3)

num_of_sum = [1]
N = int(input())
coin_1,coin_2,coin_3 = map(int,input().split())
func_1(1)
func_2(1)
func_3(1)

final_nums = set(num_of_sum)
print(len(final_nums))

