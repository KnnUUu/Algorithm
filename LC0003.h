#pragma once
#include <iostream>
#include <string>
#include <vector>
#include <assert.h> 
#include <algorithm>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        const int asciiBegin = 32, asciiEnd = 126;
        int ans = 0, temp = 0, left = 0;
        vector<int> used(asciiEnd - asciiBegin + 1,-1);
        for (size_t i = 0; i < s.size(); i++) {
            if (used[int(s[i]) - asciiBegin]!=-1) {
                left = max(left, used[int(s[i]) - asciiBegin]);
                temp = i - left;
                used[int(s[i]) - asciiBegin] = i;
                ans = max(ans, temp);
            }
            else {
                used[int(s[i]) - asciiBegin] = i;
                temp += 1;
                ans = max(ans, temp);
            }
        }
        return ans;
    }

    void test() {
        assert(lengthOfLongestSubstring("abcabcbb") == 3);
        assert(lengthOfLongestSubstring("bbbbb") == 1);
        assert(lengthOfLongestSubstring("pwwkew") == 3);
        assert(lengthOfLongestSubstring("") == 0);
        assert(lengthOfLongestSubstring("abba") == 2);
    }
};

