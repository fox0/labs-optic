import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('img.png')
MAGIC = 645
ysize, xsize, _ = img.shape

plt.imshow(img)
plt.xticks(np.arange(0, xsize, MAGIC), labels=np.arange(0, 1000, 100))
plt.yticks(np.arange(0, ysize, MAGIC), labels=np.arange(0, 1000, 100))


result1 = []
result2 = []

# горизонтальные линии
for xxx in range(10):
    y = int(ysize * (xxx / 10))

    ls1 = [(0, 0)]
    ls2 = [(0, 0)]
    for x, (v, _, _) in enumerate(img[y]):
        if 240 < v:
            line_begin, line_end = ls1[-1]
            if line_end + 1 == x:
                ls1[-1] = line_begin, x
            else:
                ls1.append((x, x))
        elif 150 < v:
            line_begin, line_end = ls2[-1]
            if line_end + 1 == x:
                ls2[-1] = line_begin, x
            else:
                ls2.append((x, x))

    for line_begin, line_end in ls1:
        plt.plot((line_begin, line_end), (y, y), 'r')
    for line_begin, line_end in ls2:
        plt.plot((line_begin, line_end), (y, y), 'g')

    print(ls1)
    print(ls2)

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

    ls1 = [(0, 0)]
    ls2 = [(0, 0)]
    for x, (v, _, _) in enumerate(img[:,y]):
        if 240 < v:
            line_begin, line_end = ls1[-1]
            if line_end + 1 == x:
                ls1[-1] = line_begin, x
            else:
                ls1.append((x, x))
        elif 150 < v:
            line_begin, line_end = ls2[-1]
            if line_end + 1 == x:
                ls2[-1] = line_begin, x
            else:
                ls2.append((x, x))

    for line_begin, line_end in ls1:
        plt.plot((y, y), (line_begin, line_end), 'r')
    for line_begin, line_end in ls2:
        plt.plot((y, y), (line_begin, line_end), 'g')


print(result1)
print(result2)

print(sum(result1) / len(result1))
print(sum(result2) / len(result2))

plt.show()


plt.subplot(211)
plt.hist(result1, 5, density=True, facecolor='g', alpha=0.75)
plt.yticks([])
plt.subplot(212)
plt.yticks([])
plt.hist(result2, 5, density=True, facecolor='g', alpha=0.75)

plt.show()