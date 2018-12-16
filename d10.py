import numpy as np
import matplotlib.pyplot as plt

ex = False

if ex:
    text_file = open('d10ex.txt', 'r')
else:
    text_file = open('d10.txt', 'r')
lines = text_file.read().split('\n')

data = [i for i in lines[:-1]]

for i in data:
    print i
    
x = []
y = []
vel = []


if ex:
    x0 = 10
    x1 = 12
    y0 = 14
    y1 = 16
    v0 = -7
    v1 = -5
    v2 = -3
    v3 = -1
else:
    x0 = 10
    x1 = 16
    y0 = 18
    y1 = 24
    v0 = -7
    v1 = -5
    v2 = -3
    v3 = -1

for i in data:
    print i
    x.append(int(i[x0:x1]))
    y.append(int(i[y0:y1]))
    vel.append((int(i[v0:v1]), int(i[v2:v3])))


for t in range(10225):
    print t
    x = [i+vel[k][0] for k,i in enumerate(x)]
    y = [i+vel[k][1] for k,i in enumerate(y)]

print ''
for t in range(10225,10227):
    print t
    x = [i+vel[k][0] for k,i in enumerate(x)]
    y = [i+vel[k][1] for k,i in enumerate(y)]

    plt.scatter(x,y, marker='x')
    plt.xlim(100,180)
    plt.ylim(100,200)
    plt.pause(5.0)
    plt.cla()


# 10227 seconds
