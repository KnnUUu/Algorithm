## 遍历 
## time O(2**N)
## space O(N) 遍历中途最多需要的栈
class SlowSolution:
    def numDecodings(self, s: str) -> int:
        if(len(s)<1):
            return 0
        
        #print(s + '-> ' + str(self.numDecodingFrom(s,0)))

        return self.numDecodingFrom(s,0)
    
    def numDecodingFrom(self, s, start):
        if start>=len(s):
            return 1
        elif s[start] == '0':
            return 0
        
        ret = 0
        # 1~9
        ret += self.numDecodingFrom(s,start+1)
        # 10~26 
        # 注意不要写成 s[start]<='2' and '0'<=s[start+1]<='6'，17 18 19判定错误
        if start+1<len(s) and (s[start]=='1' or (s[start]=='2' and '0'<=s[start+1]<='6')):
            ret += self.numDecodingFrom(s,start+2)
        return ret
    
# 保存以前结果避免重复计算
# time O（N） 每个点只需要走一次
# space O（N） 每个点需要保存一次
class Solution:
    def numDecodings(self, s: str) -> int:
        if(len(s)<1):
            return 0
        
        #print(s + '-> ' + str(self.numDecodingFrom(s,0)))

        store=dict()
        return self.numDecodingFrom(s,0,store)
    
    def numDecodingFrom(self, s, start,store):
        if start in store:
            return store[start]
        elif start>=len(s):
            store[start]=1
            return 1
        elif s[start] == '0':
            store[start]=0
            return 0
        
        ret = 0
        # 1~9
        ret += self.numDecodingFrom(s,start+1,store)
        # 10~26 
        # 注意不要写成 s[start]<='2' and '0'<=s[start+1]<='6'，17 18 19判定错误
        if start+1<len(s) and (s[start]=='1' or (s[start]=='2' and '0'<=s[start+1]<='6')):
            ret += self.numDecodingFrom(s,start+2,store)
        store[start]=ret
        return ret

test = Solution()
assert(test.numDecodings("12")==2)
assert(test.numDecodings("226")==3)
assert(test.numDecodings("06")==0)
assert(test.numDecodings("")==0)
assert(test.numDecodings("1")==1)
assert(test.numDecodings("27")==1)
assert(test.numDecodings("10")==1)
assert(test.numDecodings("2611055971756562")==4)