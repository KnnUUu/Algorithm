#pragma once

#include <iostream>
#include <string>
#include <vector>
#include <assert.h> 
#include <algorithm>

using namespace std;

class Solution {
public:
    //brute force
    // need to calculate squr(2*candies-1)-1 times, so time complex is O(squr(candies))
    /*
    vector<int> distributeCandies(int candies, int num_people) {
        int index = 0;
        int count = 1;
        vector<int> ans = vector<int>(num_people,0);
        if (candies == 0) return ans;
        while (candies > 0) {
            ans[index] += min(count, candies);
            candies -= min(count, candies);
            index += 1;
            index %= num_people;
            count += 1;
        }
        return ans;
    }
    */

    // math
    // https://leetcode.com/problems/distribute-candies-to-people/discuss/324215/Java-O(num_people)-one-pass-Math-Solution-solving-quadratic-function
    // time complex O(num_people)
#define PRINT_LOG
    vector<int> distributeCandies(int candies, int num_people) {
        int lastAdd = int(sqrt(8.0 * candies + 1.0)/2.0 - 1.0 / 2.0);
        int leftCandies = candies - lastAdd*(lastAdd + 1) / 2;
        int rounds = lastAdd / num_people; // 0 base
        int lastRoundAddTimes = lastAdd % num_people;

#ifdef PRINT_LOG
        cout << lastAdd << endl;
        cout << leftCandies << endl;
        cout << rounds << endl;
        cout << lastRoundAddTimes << endl;
#endif // PRINT_LOG

        vector<int> ans = vector<int>(num_people, 0);
        for (int i = 0; i < num_people; i++){
            if (i < lastRoundAddTimes) {
                ans[i] += (2 * i + 2 + rounds*num_people)*(rounds + 1) / 2;
            }
            else if (i == lastRoundAddTimes) {
                ans[i] += (2 * i + 2 + (rounds - 1)*num_people)*rounds / 2 + leftCandies;
            }
            else {
                ans[i] += (2 * i + 2 + (rounds - 1)*num_people)*rounds / 2;
            }
        }
#ifdef PRINT_LOG
        for (int num : ans) {
            cout << num;
        }
        cout << endl;
#endif // PRINT_LOG
        return ans;
    }

    void test() {
        assert(distributeCandies(10, 3) == vector<int>({ 5, 2, 3 }));
        assert(distributeCandies(7, 4) == vector<int>({1,2,3,1})); 
        
        std::cout << "all test passed." << std::endl;
    }
}; 