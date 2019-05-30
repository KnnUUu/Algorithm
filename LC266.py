def canPermutePalindrome(s):
    dic = set()
    for char in s:
        if char in dic:
            dic.remove(char)
        else:
            dic.add(char)
    return len(dic)<=1

print(canPermutePalindrome('code'))
print(canPermutePalindrome('aab'))
print(canPermutePalindrome('carerac'))