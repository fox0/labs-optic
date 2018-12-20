#!/usr/bin/env python3
import logging

import numpy as np
import cv2
from matplotlib import pyplot as plt

log = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s [%(levelname)s] %(funcName)s:%(name)s:%(lineno)d: %(message)s',
                    level=logging.DEBUG)

# число пикселей в 100 *мкм*
MAGIC_CONST = 645

LIMITS = (
    240,  # r
    160,  # g
    20,  # b
)

img = cv2.imread('img.png')
ysize, xsize, _ = img.shape

plt.imshow(img)
plt.xticks(np.arange(0, xsize, MAGIC_CONST), labels=np.arange(0, 1000, 100))
plt.yticks(np.arange(0, ysize, MAGIC_CONST), labels=np.arange(0, 1000, 100))
plt.xlabel('мкм')
plt.ylabel('мкм')

result0, result1, result2 = [], [], []


def get_lists(iterable):
    # списки с отрезками
    ls0, ls1, ls2 = [(0, 0)], [(0, 0)], [(0, 0)]
    for x, (v, _, _) in enumerate(iterable):
        if LIMITS[0] < v:
            ls = ls0
        elif LIMITS[1] < v:
            ls = ls1
        elif LIMITS[2] < v:
            ls = ls2
        else:
            continue
        line_begin, line_end = ls[-1]
        if line_end + 1 == x:
            ls[-1] = line_begin, x
        else:
            ls.append((x, x))
    ls0.pop(0)
    ls1.pop(0)
    ls2.pop(0)
    return ls0, ls1, ls2


# горизонтальные линии
for xxx in range(10):
    y = int(ysize * (xxx / 10))
    ls0, ls1, ls2 = get_lists(img[y])
    for ls, color in (ls0, 'r'), (ls1, 'g'), (ls2, 'b'):
        log.debug(ls)
        for line_begin, line_end in ls:
            plt.plot((line_begin, line_end), (y, y), color)

    sum0 = 0.0
    for line_begin, line_end in ls0:
        sum0 += line_end - line_begin
    result0.append(sum0 / xsize)
    sum1 = 0.0
    for line_begin, line_end in ls1:
        sum1 += line_end - line_begin
    result1.append(sum1 / xsize)
    sum2 = 0.0
    for line_begin, line_end in ls2:
        sum2 += line_end - line_begin
    result2.append(sum2 / xsize)

for xxx in range(10):
    y = int(80 + xsize * (xxx / 10))

    ls0, ls1, ls2 = get_lists(img[:, y])
    for ls, color in (ls0, 'r'), (ls1, 'g'), (ls2, 'b'):
        log.debug(ls)
        for line_begin, line_end in ls:
            plt.plot((y, y), (line_begin, line_end), color)

    sum0 = 0.0
    for line_begin, line_end in ls0:
        sum0 += line_end - line_begin
    result0.append(sum0 / ysize)
    sum1 = 0.0
    for line_begin, line_end in ls1:
        sum1 += line_end - line_begin
    result1.append(sum1 / ysize)
    sum2 = 0.0
    for line_begin, line_end in ls2:
        sum2 += line_end - line_begin
    result2.append(sum2 / ysize)

assert len(result0) == 20
assert len(result1) == 20
assert len(result2) == 20

print(result0)
print(result1)
print(result2)

print(sum(result0) / len(result0))
print(sum(result1) / len(result1))
print(sum(result2) / len(result2))

plt.show()
