#pragma once

#include <iostream>
#include <string>
#include <vector>
#include <assert.h> 
#include <algorithm>

using namespace std; 

class Solution {
public:
    int tribonacci(int n) {
        if (n == 0) { return 0; }
        else if (n == 1 || n == 2) { return 1; }

        int zero = 0, one = 1, two = 1;
        while (n >= 3) {
            int temp = zero+one+two;
            zero = one;
            one = two;
            two = temp;
            n -= 1;
        }
        return two;
    }

    void test() {
        assert(tribonacci(0) == 0);
        assert(tribonacci(1) == 1);
        assert(tribonacci(2) == 1);
        assert(tribonacci(4) == 4);
        assert(tribonacci(25) == 1389537);
        std::cout << "all test passed." << std::endl;
    }
};
