#include <assert.h> 
#include <map>
class Solution {
public:
    double myPow(double x, int n) {
        auto pair = map.find(n);
        if (pair!=map.end()){
            return pair->second;
        }

        if (n == 0) map[n] = 1;
        else if (n == 1) map[n] = x;
        else if (n % 2 == 0)  map[n] = myPow(x, n / 2) * myPow(x, n / 2);
        else if (n > 0) map[n] = myPow(x, n - 1)*x;
        else map[n] =  myPow(x, n + 1)/x;

        return map[n];
    }

    std::map<int, double> map;

    void test() {
        assert(myPow(1.0, 0) == 1);
        assert(myPow(2.0, 10) == 1024.0);
        assert(myPow(2.0, -2) == 0.25000);
    }
};

