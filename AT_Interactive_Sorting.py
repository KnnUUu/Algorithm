def merge(l, r):
    print(l)
    print(r)
    if len(l)==0: return r
    elif len(r)==0: return l
    m = ''
    l_p, r_p = 0, 0
    while 1:
        print('? ' + l[l_p] + ' ' + r[r_p],flush=True)
        if input()=='<':
            m += l[l_p]
            l_p+=1
            if l_p==len(l):
                print(m+r[r_p:])
                return m+r[r_p:]
        else:
            m += r[r_p]
            r_p+=1
            if r_p==len(r):
                print(m+l[l_p:])
                return m+l[l_p:]

N, Q = map(int,input().split())

def m_sort(string):
    if len(string)<2: return string
    mid = (len(string)+1)//2
    return merge(m_sort(string[:mid]),m_sort(string[mid:]))

print('! '+''.join([chr(ord('A')+i) for i in range(N)]))
print('! '+m_sort(''.join([chr(ord('A')+i) for i in range(N)])))