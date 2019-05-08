def isMatch(s,p):
    def dynamic(i,j):
        if i<len(s) and j>=len(p):
            return False

        elif i>=len(s) and j<len(p):
            even = j+1
            while even<len(p):
                if p[even]=='*':
                    even += 2
                else:
                    return False
            return even==len(p)-1

        elif i>=len(s) and j>=len(p):
            return True

        else:
            if j+1<len(p) and p[j+1]=='*':
                if p[j]=='.':
                    return True
                else:
                    for k in range(i,len(s)):
                        if s[k]!=p[j]:
                            break
                        elif dynamic(k,j+2):
                            return True
                    return dynamic(i,j+2)

            else:
                if s[i]==p[j] or p[j]=='.':
                    return dynamic(i+1,j+1)
                else:
                    return False

    return dynamic(0,0)

print(isMatch(s = "aa", p = "a")) # false
print(isMatch(s = "aa", p = "a*")) # true
print(isMatch(s = "ab", p = ".*")) # true
print(isMatch(s = "aab", p = "c*a*b")) # true
print(isMatch(s = "mississippi", p = "mis*is*p*.")) # false