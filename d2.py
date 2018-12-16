import numpy as np

text_file = open("d2.txt", "r")
lines = text_file.read().split('\n')

boxes = lines[:-1]

# two_total = 0
# three_total = 0
# for i in boxes:
#     print i
#     for k in i:
#         if i.count(k) == 2:
#             two_total = two_total + 1
#             break
#     for k in i:
#         if i.count(k) == 3:
#             three_total = three_total + 1
#             break



# box_total = two_total * three_total
# print box_total

import difflib
print ''
for k,i in enumerate(boxes):
    a = difflib.get_close_matches(i, boxes[0:k]+boxes[k+1:], 1,0.95)
    if len(a)>0:
        print k
        print i
        print a[0]

