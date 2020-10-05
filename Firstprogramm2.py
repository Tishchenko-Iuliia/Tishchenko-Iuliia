#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math  # импорт библиотеки math
import numpy  # импорт библиотеки numpy
import matplotlib.pyplot as mpp    # импорт библиотеки matplotlib и присваивание ей короткого имени

# Эта программа рисует график функции, заданной выражением ниже

if __name__=='__main__':   # аналог begin на pascal
    arguments = numpy.r_[0:200:0.1]
    mpp.plot(
        arguments,
        [math.sin(a) * math.sin(a/20.0) for a in arguments]
    )  # построение графика
    mpp.show()  # вывод графика 