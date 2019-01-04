import numpy as np
import collections

score0 = 3
score1 = 7


loc0 = 0
loc1 = 1

scores = []
scores.append(score0)
scores.append(score1)

### PART 1

# rec = 10
# # length = 607331
# length = 2018


# while len(scores)<length+rec:
#     score = sum([score0,score1])
#     score_add = [int(i) for i in str(score)]
#     scores.extend(score_add) 


#     # finding score0
#     rotate0 = score0+1
#     loc0 += rotate0
#     loc0 = loc0 % len(scores)
#     score0 = scores[loc0]

#     # finding score1
#     rotate1 = score1+1
#     loc1 += rotate1
#     loc1 = loc1 % len(scores)
#     score1 = scores[loc1]

# result = scores[length:length+rec]
# res = [str(r) for r in result]
# print ''.join(res)

### PART 2

rec = 10
# length = 607331
length = 30000000
inp = '607331'


while len(scores)<length+rec:
    score = sum([score0,score1])
    score_add = [int(i) for i in str(score)]
    scores.extend(score_add) 


    # finding score0
    rotate0 = score0+1
    loc0 += rotate0
    loc0 = loc0 % len(scores)
    score0 = scores[loc0]

    # finding score1
    rotate1 = score1+1
    loc1 += rotate1
    loc1 = loc1 % len(scores)
    score1 = scores[loc1]

res = [str(r) for r in scores]
resstring = ''.join(res)
idx = resstring.find(inp)
print idx
### Took around a minute on Macbook Pro. Consider checking periodically in the lloop instead


