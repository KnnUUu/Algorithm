#pragma once

#include <iostream>
#include <string>
#include <vector>
#include <assert.h> 
#include <algorithm>

using namespace std;

class Solution {
public:
    bool isPowerOfTwo(int n) {
        if (n < 1) {
            return false;
        }
        while (n!=1){
            std::cout << n << std::endl;
            if (n % 2 != 0) {
                return false;
            }
            n = n/2;
        }
        return true;
    }

    void test() {
        assert(isPowerOfTwo(-1) == false);
        assert(isPowerOfTwo(1) == true);
        assert(isPowerOfTwo(16) == true);
        assert(isPowerOfTwo(3) == false);
        assert(isPowerOfTwo(4) == true);
        assert(isPowerOfTwo(5) == false);
        std::cout << "all test passed." << std::endl;
    }
};