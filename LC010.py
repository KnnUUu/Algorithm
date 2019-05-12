def isMatch(s,p):
    if not p: return not s # empty pattern
    if not s: # empty string
        if len(p)>=2 and p[1]=='*':
            return isMatch(s,p[2:])
        else:
            return False

    firstMatch = s[0] == p[0] or p[0]=='.'
    star = len(p)>=2 and p[1]=='*'

    if firstMatch:
        if star:
            return isMatch(s[1:],p) or isMatch(s,p[2:])
        else:
            return isMatch(s[1:],p[1:])
    else:
        if star:
            return isMatch(s,p[2:])
        else:
            return False

def isMatch(s,p):
    def dp(i,j):
        if j>=len(p):
            return i>=len(s)
        if i>=len(s):
            if j+1<len(p) and p[j+1]=='*':
                return dp(i,j+2)
            else:
                return False

        firstMatch = s[i] == p[j] or p[j]=='.'
        star = j+1<len(p) and p[j+1]=='*'

        if firstMatch:
            if star:
                return dp(i+1,j) or dp(i,j+2)
            else:
                return dp(i+1,j+1)
        else:
            if star:
                return dp(i,j+2)
            else:
                return False
    return dp(0,0)

def isMatch(s,p):
    memory = dict()
    def dp(i,j):
        if (i,j) in memory: return memory[i,j]

        if j>=len(p):
            memory[i,j]=i>=len(s)
            return memory[i,j]
        if i>=len(s):
            if j+1<len(p) and p[j+1]=='*':
                return dp(i,j+2)
            else:
                memory[i, j] =False
                return memory[i,j]

        firstMatch = s[i] == p[j] or p[j]=='.'
        star = j+1<len(p) and p[j+1]=='*'

        if firstMatch:
            if star:
                return dp(i+1,j) or dp(i,j+2)
            else:
                return dp(i+1,j+1)
        else:
            if star:
                return dp(i,j+2)
            else:
                memory[i, j] = False
                return memory[i, j]
    return dp(0,0)

print(isMatch(s = "aa", p = "a")) # false
print(isMatch(s = "aa", p = "a*")) # true
print(isMatch(s = "ab", p = ".*")) # true
print(isMatch(s = "aab", p = "c*a*b")) # true
print(isMatch(s = "mississippi", p = "mis*is*p*.")) # false
print(isMatch(s = "ab", p = ".*c")) # false