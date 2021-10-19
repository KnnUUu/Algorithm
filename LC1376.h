#pragma once

#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <assert.h> 
#include <algorithm>
#include <queue>

using namespace std;

#define DEBUG

class Solution {
public:
    int numOfMinutes(int n, int headID, vector<int>& manager, vector<int>& informTime) {
        map<int, vector<int>> subordinates;
        for (auto i = 0; i < manager.size(); i++) {
            if (manager[i]!=-1) {
                subordinates[manager[i]].push_back(i);
            }
        }
#ifdef DEBUG
        for (auto it = subordinates.begin(); it != subordinates.end(); it++) {
            cout << it->first << ":";
            for(int sub : it->second) cout << sub << " ";
        }
        cout << endl;
#endif // DEBUG

        int ans = 0;
        recusion(headID, subordinates, informTime, informTime[headID], ans);
#ifdef DEBUG
        cout << ans;
        cout << endl;
#endif // DEBUG
        return ans;
    }

    void recusion(int id, map<int, vector<int>>& subordinates, vector<int>& informTime, int sum,int& ans) {
        if (subordinates.find(id) == subordinates.end()) {
            ans = max(ans, sum);
        }
        else {
            for (int subID : subordinates[id]) {
                recusion(subID, subordinates, informTime, sum + informTime[subID], ans);
            }
        }
    }

    void test() {
        assert(numOfMinutes(1, 0, vector<int>({ -1 }), vector<int>({ 0 })) == 0);
        assert(numOfMinutes(6, 2, vector<int>({ 2,2,-1,2,2,2 }), vector<int>({ 0,0,1,0,0,0 })) == 1);
        assert(numOfMinutes(7, 6, vector<int>({ 1, 2, 3, 4, 5, 6, -1 }), vector<int>({ 0, 6, 5, 4, 3, 2, 1 })) == 21);
        assert(numOfMinutes(15, 0, vector<int>({ -1,0,0,1,1,2,2,3,3,4,4,5,5,6,6 }), vector<int>({ 1,1,1,1,1,1,1,0,0,0,0,0,0,0,0 })) == 3);
        assert(numOfMinutes(4, 2, vector<int>({ 3,3,-1,2 }), vector<int>({ 0,0,162,914 })) == 1076);
        assert(numOfMinutes(8, 0, vector<int>({ -1,5,0,6,7,0,0,0 }), vector<int>({ 89,0,0,0,0,523,241,519 })) == 612);
        std::cout << "all test passed." << std::endl;
        system("pause");
    }
};
