#pragma once

#include <iostream>
#include <string>
#include <vector>
#include <assert.h> 
#include <algorithm>

using namespace std;

class Solution {
public:
    int numDecodings(string s) {
        std::vector<unsigned int> dp(s.size()+1);
        dp[0] = 1;
        dp[1] = s[0] == '0' ? 0 : 1;
        for (int i = 2; i <= s.size(); i++){
            if (0 < s[i - 1] - '0' && s[i - 1] - '0' <= 9) {
                dp[i] += dp[i - 1];
            }
            if (10 <= stoi(s.substr(i - 2, 2)) && stoi(s.substr(i - 2, 2)) <= 26) {
                dp[i] += dp[i - 2];
            }
        }
        return dp[s.size()];
    }
    
    
    /*
    int ans = 0;
    int char0int = int('0');
    bool lengthCondition;
    bool firstCharCondition;
    bool secondCharCondition;

    int numDecodings(string s) {
        ans = 0;
        countFromIndex(0, s);
        return ans;
    }
    void countFromIndex(int i,string &s) {
        if (i >= s.size()) {
            ans += 1;
            return;
        }
        // one character
        if (s[i] >= '1' && s[i] <= '9') {
            countFromIndex(i+1, s);
        }
        // two charactor
        lengthCondition = (i+1 < s.size());
        firstCharCondition = (s[i] == '1' || s[i] == '2');
        secondCharCondition = (s[i + 1] <= '6' && s[i + 1] >= '0');
        if (lengthCondition && firstCharCondition && secondCharCondition) {
            countFromIndex(i+2, s);
        }

        // start from 0
        lengthCondition = (i + 1 < s.size());
        firstCharCondition = (s[i] == '0');
        secondCharCondition = (s[i + 1] <= '9' && s[i + 1] >= '0');
        if (lengthCondition && firstCharCondition && secondCharCondition) {
            countFromIndex(i + 2, s);
        }
    }
    */
    void test() {
        assert(numDecodings("12") == 2);
        assert(numDecodings("226") == 3);
        assert(numDecodings("0") == 0);
        assert(numDecodings("000") == 0);
        assert(numDecodings("1") == 1);
        assert(numDecodings("2611055971756562") == 4);
    }
};