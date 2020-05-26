#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Дан набор из N долей, представленных в виде N рациональных.
Необходимо представить эти доли в процентном выражении c точностью до трех знаков после запятой.
"""
from decimal import Decimal, localcontext
from typing import List


def get_decimals_from_fractions(fractions: List[float]) -> tuple:
    """
    >>> get_decimals_from_fractions([1.5, 3, 6, 1.5])
    (0.125, 0.250, 0.500, 0.125)
    """
    input_length = len(fractions)

    if sum(fractions) == 0 or input_length == 0:
        raise Exception('Fractions should contain at least one positive value')

    if any([f < 0 for f in fractions]):
        raise NotImplementedError

    with localcontext() as ctx:
        ctx.prec = 3
        s = sum(fractions)
        return tuple(Decimal(f / s) for f in fractions)


if __name__ == '__main__':
    n = int(input())
    f_input = [float(input()) for i in range(n)]

    for d in get_decimals_from_fractions(f_input):
        print(f'{d:.3f}')
