#pragma once
#include <vector>
#include <algorithm>
#include <assert.h> 
#include <iostream>

using namespace std;
/*
Time complexity : O(n). Single pass.
Space complexity : O(1). Constant space is used.
*/
class Solution {
public:
    int maxArea(vector<int>& height) {
        int l = 0, r = height.size()-1, ans = 0;
        while (l<r){
            ans = max(ans, (r - l)*min(height[l], height[r]));
            if (height[l] > height[r]) r -= 1;
            else l += 1;
            cout << "L=" << l << " R=" << r << " ans=" << ans << endl;
        }
        return ans;
    }

    void test() {
        assert(maxArea(vector<int> { 1, 8, 6, 2, 5, 4, 8, 3, 7 }) == 49);
        assert(maxArea(vector<int> { 1,1 }) == 1);
        assert(maxArea(vector<int> { 4,3,2,1,4 }) == 16);
        assert(maxArea(vector<int> { 1,2,1 }) == 2);
        assert(maxArea(vector<int> { 0,0 }) == 0);
    }
};
