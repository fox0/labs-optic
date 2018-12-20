#!/usr/bin/env python3
import math
import logging

log = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s [%(levelname)s] %(funcName)s:%(name)s:%(lineno)d: %(message)s',
                    level=logging.DEBUG)

result1 = [1.95, 2.68, 4.22, 2.47, 1.63]
result2 = [1.01, 1.44, 1.57, 1.41, 1.13]
result3 = [3.82, 3.43, 3.71, 1.64, 0.73969]


def get_student_k(alpha, m):
    return {
        (0.05, 4): 2.132,
        # …
        (0.05, 18): 2.101,
        (0.05, 19): 2.093,
    }[(alpha, m)]


def get_smirnov_k(alpha, n):
    """Критические значения критерия Смирнова"""
    return {
        (0.05, 5): 1.67,
        # …
        (0.05, 18): 2.50,
        (0.05, 19): 2.53,
        (0.05, 20): 2.53,
    }[alpha, n]


alpha = 0.05

for i, ls in enumerate((result1, result2, result3)):
    print('Образец %d' % (i + 1))
    while True:
        n = len(ls)
        print('1. Объём выборки = %d' % n)
        x_avr = sum(ls) / n
        print('2. Среднее выборочное арифметическое = %.3f мкм.' % x_avr)
        s_x2 = sum((x_i - x_avr) ** 2 for x_i in ls) / (n - 1)
        print('3. Выборочная дисперсия = %.3f мкм.' % s_x2)
        s_x = math.sqrt(s_x2)
        print('4. Выборочное среднее квадратичное отклонение = %.3f мкм.' % s_x)
        v = s_x / x_avr * 100
        print('5. Выборочный коэффициент вариации = %.3f%%' % v)
        m_x = x_avr
        m = n - 1
        delta = get_student_k(alpha, m) * s_x / math.sqrt(n)
        print('6. Доверительный интервал = %.3f ± %.3f мкм.' % (m_x, delta))

        print('7. Проверка на наличие в выборке грубых погрешностей по критерию Смирнова.')
        ls.sort()
        print('7.1. Нулевая гипотеза H0: среди значений нет грубых погрешностей.')
        print('7.2. Альтернативная гипотеза H1: значение %.3f в выборке является грубой погрешностью.' % ls[-1])
        u = (ls[-1] - x_avr) / s_x
        print('7.3. u = %.3f' % u)
        print('7.4. alpha = %.3f' % alpha)
        u_t = get_smirnov_k(alpha, n)
        print('7.5. u_t = %.3f' % u_t)
        if u > u_t:
            print('7.6. %.3f > %.3f = true' % (u, u_t))
            print('''7.7. Поскольку значение статистики попало в критическую область, то нулевая гипотеза \
отвергается и в качестве рабочей принимается альтернативная. Пересчёт…''')
            del ls[-1]
            continue
        else:
            print('7.6. %.3f > %.3f == false' % (u, u_t))
            print('7.7. Принимается нулевая гипотеза.')

        # todo копипаста :)
        print('7. Проверка на наличие в выборке грубых погрешностей по критерию Смирнова.')
        ls.sort()
        print('7.1. Нулевая гипотеза H0: среди значений нет грубых погрешностей.')
        print('7.2. Альтернативная гипотеза H1: значение %.3f в выборке является грубой погрешностью.' % ls[0])
        u = (x_avr - ls[0]) / s_x
        print('7.3. u = %.3f' % u)
        print('7.4. alpha = %.3f' % alpha)
        u_t = get_smirnov_k(alpha, n)
        print('7.5. u_t = %.3f' % u_t)
        if u > u_t:
            print('7.6. %.3f > %.3f = true' % (u, u_t))
            print('''7.7. Поскольку значение статистики попало в критическую область, то нулевая гипотеза \
отвергается и в качестве рабочей принимается альтернативная. Пересчёт…''')
            del ls[0]
            continue
        else:
            print('7.6. %.3f > %.3f == false' % (u, u_t))
            print('7.7. Принимается нулевая гипотеза.')
        break
