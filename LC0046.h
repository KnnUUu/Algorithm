#pragma once
#include <iostream>
#include <vector>
#include <assert.h> 
using namespace std;

class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> ans = {};
        permuteDynamic(0,nums,ans);
        return ans;
    }

    void permuteDynamic(size_t startIndex, vector<int>& nums, vector<vector<int>>& ans){
        if (startIndex >= nums.size()) {
            ans.push_back(nums);
            return;
        }
        for (size_t i = startIndex; i < nums.size(); i++){
            swap(nums[startIndex], nums[i]);
            permuteDynamic(startIndex + 1, nums, ans);
            swap(nums[startIndex], nums[i]);
        }
    }

    void test() {
        vector<int> input1 = {1,2,3};
        vector<vector<int>> output1 = 
        {
            {1,2,3},
            {1,3,2},
            {2,1,3},
            {2,3,1},
            {3,1,2},
            {3,2,1}
        };
        assert(permute(input1)==output1);
    }
};