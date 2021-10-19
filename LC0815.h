#pragma once

#include <iostream>
#include <unordered_map>
#include <vector>
#include <queue>
#include <assert.h> 
#include <algorithm>
#include<set>

using namespace std;

class Solution {
public:
    int numBusesToDestination(vector<vector<int>>& routes, int source, int target) {
        // all routes contain stop
        unordered_map<int, vector<int>> stop2busRoutes;
        for (int busIndex = 0; busIndex < routes.size(); busIndex++) {
            for (int stop : routes[busIndex]) {
                stop2busRoutes[stop].push_back(busIndex);
            }
        }

        // stop , tripCount
        queue<pair<int,int>> bfs;
        set<int> checked;
        bfs.push({ source ,0 });
        while (!bfs.empty()){
            int stop = bfs.front().first;
            int tripCount = bfs.front().second;
            bfs.pop();
            checked.insert(stop);
            if (stop == target) {
                return tripCount;
            }

            vector<int> busRoutes = stop2busRoutes[stop];
            for (int busIndex : busRoutes) {
                for (int nextStop : routes[busIndex]) {
                    // not in set
                    if (checked.find(nextStop) == checked.end()) {
                        bfs.push({ nextStop,tripCount + 1 });
                    }
                }
                routes[busIndex].clear();
            }
        }
        return -1;
    }
    void test() {
        assert(numBusesToDestination(vector<vector<int>>({{1, 2, 7}, {3, 6, 7}}), 1, 6) == 2);
        assert(numBusesToDestination(vector<vector<int>>({ { 1, 2, 7 },{ 3, 6, 7 } }), 1, 1) == 0);
        assert(numBusesToDestination(vector<vector<int>>({{7, 12},{4, 5, 15},{6},{15, 19},{9, 12, 13}}), 15, 12) == -1);
        std::cout << "all test passed." << std::endl;
    }
};
