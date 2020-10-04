Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #!/usr/bin/env python3^M
   ...: # -*- coding: utf-8 -*-^M
   ...: ^M
   ...: import math^M   # импорт библиотеки math
   ...: import numpy^M   # импорт библиотеки numpy
   ...: import matplotlib.pyplot as mpp^M   # импорт библиотеки matplotlib и присваивание ей короткого имени
   ...: ^M
   ...: # Эта программа рисует график функции, заданной выражением ниже^M
   ...: ^M
   ...: if __name__=='__main__':^M  # аналог begin на pascal
   ...:     arguments = numpy.r_[0:200:0.1]^M
   ...:     mpp.plot(^M
   ...:         arguments,^M
   ...:         [math.sin(a) * math.sin(a/20.0) for a in arguments]^M
   ...:     )^M  # построение графика
   ...:     mpp.show()  # вывод графика         