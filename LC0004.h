#pragma once
#include <iostream>
#include <string>
#include <vector>
#include <assert.h> 
#include <algorithm>

using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        // nums1.size() must smaller than nums2.size()
        if (nums1.size() > nums2.size()) { nums1.swap(nums2); }

        // 0 <= i <= len(nums1) 
        // seperate nums1 with nums[i-1] and nums[i]
        // length are i and len(num1)-i
        int iMin = 0, iMax = nums1.size(), halfLen = (nums2.size()+ nums1.size()+1)/2;
        int i, j, leftMax, rightMin;
        while (iMin<=iMax){
            i = (iMax + iMin) / 2;
            j = halfLen - i;
            // nums1[i-1] too big, move left
            if (i>0 && nums1[i-1] > nums2[j]) {
                iMax = i-1;
            }
            else if (i < nums1.size() && nums1[i] < nums2[j-1]) {
                iMin = i + 1;
            }
            else {
                if (i == 0) { leftMax = nums2[j - 1]; }
                else if (j == 0) { leftMax = nums1[i - 1]; }
                else { leftMax = max(nums1[i - 1], nums2[j - 1]); }
                
                if ((nums2.size() + nums1.size()) % 2 != 0) {
                    return float(leftMax);
                }

                if (i == nums1.size()) { rightMin = nums2[j]; }
                else if (j == nums2.size()) { rightMin = nums1[i]; }
                else { rightMin = min(nums1[i], nums2[j]); }

                return (leftMax + rightMin) / 2.0;
            }
        }
        return 0.0;
    }

    void test() {
        assert(findMedianSortedArrays(vector<int> {1,3}, vector<int> {2}) == 2.0);
        assert(findMedianSortedArrays(vector<int> {1, 2}, vector<int> {3, 4}) == 2.5);
        assert(findMedianSortedArrays(vector<int> {0,0}, vector<int> {0,0}) == 0.0);
        assert(findMedianSortedArrays(vector<int> {}, vector<int> {1}) == 1.0);
        assert(findMedianSortedArrays(vector<int> {2}, vector<int> {}) == 2.0);
    }
};