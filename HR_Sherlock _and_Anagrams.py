import math
def sherlockAndAnagrams(s:str):
    counter = dict()
    for index in range(len(s)):
        for strlen in range(1, len(s)-index+1):
            key = ''.join(sorted(s[index:index+strlen]))
            if key not in counter:
                counter[key]=1
            else:
                counter[key]+=1
    
    ret = 0
    for key, val in counter.items():
        ret += math.comb(val,2)
    return ret

print(''.join(sorted("apple")))