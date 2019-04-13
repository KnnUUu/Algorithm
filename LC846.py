def isNStraightHand(hand,W):
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

print(isNStraightHand(hand = [1,2,3,6,2,3,4,7,8], W = 3)) #true

print(isNStraightHand(hand = [1,2,3,4,5], W = 4))# false

print(isNStraightHand(hand = [1,2,2,3,3,4], W = 3))# true

print(isNStraightHand(hand = [0], W = 4))# false

print(isNStraightHand([1,1,2,2,3,3], 2))# false
