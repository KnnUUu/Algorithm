#pragma once

#include <iostream>
#include <string>
#include <vector>
#include <assert.h> 
#include <algorithm>
#include <cmath>

using namespace std;

class Solution {
public:
    double champagneTower(int poured, int query_row, int query_glass) {
        double ans[100][100] = { 0.0 };
        ans[0][0] = poured;
        for (int i = 0; i <= min(query_row,98); i++){
            for (int j = 0; j <= i; j++) {
                if (ans[i][j]>1){
                    ans[i + 1][j] += (ans[i][j] - 1) / 2.0;
                    ans[i + 1][j+1] += (ans[i][j] - 1) / 2.0;
                    ans[i][j] = 1;
                }
            }
        }
        return ans[query_row][query_glass];
    }

    void test() {
        assert(champagneTower(1, 1, 1) == 0.00000);
        assert(champagneTower(2, 1, 1) == 0.50000);
        assert(champagneTower(100000009, 33, 17) == 1.0000);
        std::cout << "all test passed." << std::endl;
    }
};