def getSkyline(buildings) :

    if len(buildings)==0: return []
    elif len(buildings)==1: return [[buildings[0][0],buildings[0][2]]]

    ans = [[buildings[0][0],buildings[0][2]]]
    for i in range(len(buildings)-1):
        if buildings[i][2] > buildings[i+1][2]:
            if buildings[i][0]==buildings[i+1][0]:

            elif buildings[i][1]bdildings[i+1][0]:

            else:
        elif buildings[i][2] < buildings[i+1][2]:

        else: # H(i)==H(i+1)

buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]

print(getSkyline())