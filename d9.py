import numpy as np
import collections

#input = 416 players; last marble is worth 71975 points


# players = 9
# high = 25

# players = 10
# high = 1618


# players = 13
# high = 7999

players = 416
high = 7197500



#### PART 1

# circle = [0]

# score = {}

# for p in range(players):
#     score[p+1] = 0
    
# player = 1
# k = 0
# for i in range(high):
#     marble_no = i+1
#     if k+2>len(circle):
#         marble_loc = k+2-len(circle)
#     else:
#         marble_loc = k+2
#     if marble_no % 23 == 0:
#         marble_loc_sc = marble_loc-2-7
#         if marble_loc_sc<0:
#             marble_loc_up = len(circle)+marble_loc_sc
#         else:
#             marble_loc_up = marble_loc_sc
#         sc = circle[marble_loc_up]
#         score_cur = score[player]
#         score[player] = score_cur+marble_no+sc
#         marble_loc = marble_loc_up 
#         circle.pop(marble_loc_up)
#     else:
#         circle.insert(marble_loc,marble_no)
#     player +=1
#     if player>players:
#         player = 1
#     k = marble_loc



# max_key = max(score, key=score.get)
# max_val = score[max_key]

# print 'RESULT'
# print max_key
# print max_val


### PART 2


circle = collections.deque([0])

score = {}

for p in range(players):
    score[p+1] = 0
    
player = 1

for i in range(high):
    marble_no = i+1
    if i in [1,2]:
        circle.rotate(1)
    else:
        circle.rotate(-2)
    if marble_no % 23 == 0:
        circle.rotate(9)
        sc = circle[0]
        score_cur = score[player]
        score[player] = score_cur+marble_no+sc
        circle.popleft()
    else:
        if i == 0:
            circle.append(marble_no)
        else:
            circle.appendleft(marble_no)
    player +=1
    if player>players:
        player = 1



max_key = max(score, key=score.get)
max_val = score[max_key]

print 'RESULT'
print max_key
print max_val
