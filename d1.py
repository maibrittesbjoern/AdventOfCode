import numpy as np
import itertools

numbers = np.loadtxt('d1p1.txt')


total = 0
freq  = [0]

# for i in numbers:
#     print total
#     total = total+i

# print total
for i in itertools.cycle(numbers):
    total = total+i
    if total in freq:
        print total
        print 'FUNDET'
        sdfsdf
    freq.append(total)    




