#pragma once

#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <assert.h> 
#include <algorithm>

using namespace std;


//Definition for a binary tree node.

struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode() : val(0), left(nullptr), right(nullptr) {}
     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    vector<int> findFrequentTreeSum(TreeNode* root) {
        vector<int> ans = {};
        if (!root) { return ans; }

        map<int, int> counter; // count appear times for every sum <sum, appear times>
        getChildSum(*root, counter);

        for (auto it = counter.begin(); it != counter.end(); it++)
        {
            int sum = it->first, times = it->second;
            cout << "sum: " << sum << " times: " << times << endl;
            if (ans.empty() || times == counter[ans[0]]) {
                ans.push_back(sum);
            }
            else if (times > counter[ans[0]]) {
                ans.clear();
                ans.push_back(sum);
            }
        }
        return ans;
    }

    int getChildSum(TreeNode child, map<int, int> &counter) {
        int leftSum = 0, rightSum = 0;
        if (child.left) { leftSum = getChildSum(*child.left, counter); }
        if (child.right) { rightSum = getChildSum(*child.right, counter); }

        int sum = child.val + leftSum + rightSum;
        if(counter.find(sum) == counter.end()) {
            counter[sum] = 1;
        }
        else {
            counter[sum] += 1;
        }
        return sum;
    }
};