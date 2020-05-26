#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Допустим, что на рынке существует некое множество облигаций с номиналом 1000 условных единиц,
по которым каждый день выплачивается купон размером 1 уе.
Погашение номинала облигации (то есть выплата 1000 условных единиц) происходит в конце срока.

Каждая облигация на рынке характеризуется названием (некая строка) и ценой, цена выражается в
виде процентов от номинала, то есть цена 98.5 соответствует цене 98,5% * 1000 = 985 условных единиц.

У некоего трейдера есть информация о том какие предложения по облигациям будут на рынке в ближайшие N дней.
По каждому дню он знает, какие лоты будут представлены на бирже: название облигации, цену и количество в штуках.
Каждый день на рынке может быть от 0 до M лотов. Трейдер располагает суммой денежных средств в количестве S.

Необходимо определить какие лоты в какие дни нужно купить, чтобы получить максимальный доход с учетом следующих
условий:

* Трейдер может только покупать облигации. Купленные облигации не продаются.
* Трейдер может купить только весь лот целиком при наличии доступных
денежных средств.
* Выплаченные купоны по купленным облигациям не реинвестируются, то есть не
увеличивают сумму доступных денежных средств.
* Все купленные облигации будут погашены в день N+30.
* Доход рассчитывается на день N+30, то есть после погашения облигаций.
"""

cache = {}


def total_value(items, max_weight):
    return sum([x[2] for x in items]) if sum([x[1] for x in items]) <= max_weight else 0


def solve(items, max_weight):
    if not items:
        return ()
    if (items, max_weight) not in cache:
        head = items[0]
        tail = items[1:]
        include = (head,) + solve(tail, max_weight - head[1])
        not_include = solve(tail, max_weight)
        if total_value(include, max_weight) > total_value(not_include, max_weight):
            answer = include
        else:
            answer = not_include
        cache[(items, max_weight)] = answer
    return cache[(items, max_weight)]


if __name__ == '__main__':
    N, M, S = map(int, input().split())

    inp = []
    while True:
        r = input()
        if r == "":
            break
        r = r.split()
        inp.append((int(r[0]), r[1], float(r[2]), int(r[3])))

    prepared = tuple((i, int(x[2] * 10 * x[3]), x[3]) for i, x in enumerate(inp))

    result = solve(prepared, S)
    result = list(inp[index] for index, _, _ in result)

    print(- sum(map(lambda item: item[2] * 10 * item[3], result))
          + sum(map(lambda item: 1000 * item[3], result))
          + sum(map(lambda item: (30 + N - item[0]) * item[3], result)))

    for item in result:
        print(' '.join(str(x) for x in item))
    print("")
