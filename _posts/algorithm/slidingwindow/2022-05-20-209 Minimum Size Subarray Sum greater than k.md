---
layout: post
title: "[Leetcode] 209 Minimum Size Subarray Sum greater than k"
subtitle: ""
categories: algorithm
tags: slidingwindow
comments:
---

## Link: [209 Minimum Size Subarray Sum greater than k](https://leetcode.com/problems/minimum-size-subarray-sum-greater-than-k/)

```cpp
class Solution {
public:
    int minSubArrayLen(int s, vector<int>& nums) {
        if(nums.size()<=1) return nums.size();
        int start=0;
        int min_length=INT_MAX;
        int current_sum=0;
        
        for(int end=0; end<nums.size(); end++){
            current_sum+=nums[end];
            while(current_sum>=s){
                min_length=min(min_length,end-start+1);
                current_sum-=nums[start++];
            }
            
        }
        return min_length==INT_MAX ? 0 : min_length;
    }
};
```
