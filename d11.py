import numpy as np

# Find the fuel cell's rack ID, which is its X coordinate plus 10.
# Begin with a power level of the rack ID times the Y coordinate.
# Increase the power level by the value of the grid serial number (your puzzle input).
# Set the power level to itself multiplied by the rack ID.
# Keep only the hundreds digit of the power level (so 12345 becomes 3; numbers with no hundreds digit become 0).
# Subtract 5 from the power level.

# The rack ID is 3 + 10 = 13.
# The power level starts at 13 * 5 = 65.
# Adding the serial number produces 65 + 8 = 73.
# Multiplying by the rack ID produces 73 * 13 = 949.
# The hundreds digit of 949 is 9.
# Subtracting 5 produces 9 - 5 = 4

# x0=3
# y0=5
# grid=8

# x0=217
# y0=196


grid=8868

coor = np.ndarray((300,300))
coor_max = np.ndarray((300,300))


for i in range(300):
    for j in range(300):
        x = i+1
        y = j+1
        rackid = x+10
        pinit = rackid*y
        pup = pinit+grid
        pup1 = pup*rackid
        if pup1>99:
            p100 = int(str(pup1)[-3])
        else:
            p100 = 0
            
        power = p100-5
        coor[i,j] = power


for i in range(297):
    for j in range(297):
        power_max = 0
        for k in range(3):
            for l in range(3):
                power_max+=coor[i+k,j+l]

        coor_max[i,j] = power_max


print coor_max.max()
indices = np.where(coor_max == coor_max.max())
print indices[0]+1,indices[1]+1



# import matplotlib.pyplot as plt

# print ''
# l = 300
# xarray = [i for i in range(l)]*l
# yarray = []
# for i in range(l):
#     yarray.extend([i]*l)

# carray = coor.flatten()[0:l*l]

# # print len(xarray)
# # print len(yarray)
# # print len(carray)
# # print xarray
# # print yarray
# # print carray

# # plt.scatter(xarray,yarray,c=carray, cmap='jet', s=1)
# plt.scatter(xarray,yarray,c=carray, lw=0, s=0.1)
# plt.xlim([0,300])
# plt.ylim([0,300])
# plt.colorbar()
# plt.show()

