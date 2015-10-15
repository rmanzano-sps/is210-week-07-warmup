#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""build a Fibonacci sequence generator function with our while loop"""


def fibonacci(maxinit):
    lastnum, curnum = 0,1
    list = []
    while lastnum <= maxinit:
        list.append(lastnum)
        lastnum, curnum = curnum, lastnum + curnum
    return list
