def isNStraightHand_1(hand,W):
    """
    Alice has a hand of cards, given as an array of integers.

    Now she wants to rearrange the cards into groups so that each group is size W, and consists of W consecutive cards.

    Return true if and only if she can.

    :param hand:
    :param W:
    :return boolean
    """

    if len(hand)%W!=0: return False
    group_num = len(hand)//W
    hand.sort()
    for i in range(group_num):
        start_num = hand[0]
        print(hand)
        for j in range(W):
            for k in range(len(hand)):
                if hand[k] == start_num+j:
                    hand.pop(k)
                    break
                elif hand[k]>start_num+j:
                    return False

    if len(hand)==0: return True
    else: return False

import collections

def isNStraightHand_2(hand,W):
    count = collections.Counter(hand)
    while count:
        min_val = min(count)
        for i in range(W):
            if min_val+i not in count: return False
            count[min_val+i]-=1
            if count[min_val+i]==0: count.pop(min_val+i)
    return True

    print(count)
    print(min(count))

def isNStraightHand_3(hand,W):
    count = collections.Counter(hand)
    for key in sorted(count):
        if count[key]>0:
            for j in range(W-1,-1,-1):
                count[key+j]-=count[key]
                if count[key+j]<0: return False
    return True

def isNStraightHand_3(hand,W):
    c = collections.Counter(hand)
    start = collections.deque()
    last_checked, opened = -1, 0
    for i in sorted(c):
        if opened > c[i] or opened > 0 and i > last_checked + 1: return False
        start.append(c[i] - opened)
        last_checked, opened = i, c[i]
        if len(start) == W: opened -= start.popleft()
    return opened == 0

print(isNStraightHand_3(hand = [1,2,3,6,2,3,4,7,8], W = 3)) #true

print(isNStraightHand_3(hand = [1,2,3,4,5], W = 4))# false

print(isNStraightHand_3(hand = [1,2,2,3,3,4], W = 3))# true

print(isNStraightHand_3(hand = [0], W = 4))# false

print(isNStraightHand_3([1,1,2,2,3,3], 2))# false
