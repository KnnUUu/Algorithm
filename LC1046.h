#pragma once

#include <iostream>
#include <string>
#include <vector>
#include <assert.h> 
#include <algorithm>
#include <queue>

using namespace std;

#define DEBUG

class Solution {
public:
    /*
    int lastStoneWeight(vector<int>& stones) {
        sort(stones.begin(), stones.end(), greater<int>());
#ifdef DEBUG
        for (int i : stones) {
            cout << i << " ";
        }
        cout << endl;
#endif // DEBUG
        int newWeight=0;
        while (stones.size() >= 2) {
            newWeight = stones[0] - stones[1];
            stones.erase(stones.begin(), stones.begin() + 2);
            if (newWeight != 0) {
                auto insertIndex = stones.end();
                for (size_t i = 0; i < stones.size(); i++){
                    if (newWeight > stones[i]) {
                        insertIndex = stones.begin()+i;
                        break;
                    }   
                }
                stones.insert(insertIndex, newWeight);
#ifdef DEBUG
                for (int i : stones) {
                    cout << i << " ";
                }
                cout << endl;
#endif // DEBUG
            }
        }
        if (stones.size() == 1) {
            return stones[0];
        }
        else {
            return 0;
        }
    }
    */

    int lastStoneWeight(vector<int>& A) {
        priority_queue<int> pQueue;
        for (int i : A) {
            pQueue.push(i);
        }

        while (pQueue.size() > 1) {
            int x = pQueue.top();
            pQueue.pop();
            int y = pQueue.top();
            pQueue.pop();
            if (x > y) { pQueue.push(x - y); }
        }

        return pQueue.size() > 0 ? pQueue.top() : 0;
    }

    void test() {
        assert(lastStoneWeight(vector<int>({ 2,7,4,1,8,1 })) == 1);
        std::cout << "all test passed." << std::endl;
        system("pause");
    }
};