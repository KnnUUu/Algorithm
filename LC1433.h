#pragma once

#include <iostream>
#include <string>
#include <vector>
#include <assert.h> 
#include <algorithm>

using namespace std; 

#define DEBUG

class Solution {
public:
    bool checkIfCanBreak(string s1, string s2) {
        vector<int> counterS1 = vector<int>(26, 0);
        for (auto c : s1) {
            counterS1[int(c) - int('a')] += 1;
        }

        vector<int> counterS2 = vector<int>(26, 0);
        for (auto c : s2) {
            counterS2[int(c) - int('a')] += 1;
        }

#ifdef DEBUG
        for (int count:counterS1) {
            cout << count;
        }
        cout << endl;

        for (int count : counterS2) {
            cout << count;
        }
        cout << endl;
#endif // DEBUG


        if (compare(counterS1, counterS2) || compare(counterS2, counterS1)) {
            return true;
        }
        else{
            return false;
        }
    }

    bool compare(vector<int> counterS1, vector<int> counterS2) {
        // assume s1<s2
        int indexS1 = 0, indexS2 = 0;
        while (indexS1<counterS1.size() && indexS2<counterS2.size()) {
            while (indexS1<counterS1.size() && counterS1[indexS1] == 0) { 
                indexS1 += 1; 
                if (indexS1 == counterS1.size()) {
                    return true;
                }
            }
            while (indexS2<counterS2.size() && counterS2[indexS2] == 0) { 
                indexS2 += 1; 
                if (indexS2 == counterS2.size()) { 
                    return true; 
                }
            }
            if (indexS2 >= indexS1) {

                counterS1[indexS1] -= 1;
                counterS2[indexS2] -= 1;
            } else {
                return false;
            }
        }
        return true;
    }

    void test() {
        assert(checkIfCanBreak("abc", "xya") == true);
        assert(checkIfCanBreak("abe", "acd") == false);
        assert(checkIfCanBreak("leetcodee", "interview") == true);
        std::cout << "all test passed." << std::endl;
    }
};

