#pragma once

#include <iostream>
#include <string>
#include <vector>
#include <assert.h> 
#include <algorithm>

using namespace std;

class Solution {
public:
    int arrangeCoins(int n) {
        //rõ “™·”—ñ‹˜a
        return int(sqrt(2 * (long)n + 0.25) - 0.5);
    }

    void test() {
        assert(arrangeCoins(0) == 0);
        assert(arrangeCoins(5) == 2);
        assert(arrangeCoins(8) == 3);
        assert(arrangeCoins(6) == 3);
        std::cout << "all test passed." << std::endl;
    }
};