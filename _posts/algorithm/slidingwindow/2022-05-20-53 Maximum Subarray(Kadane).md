---
layout: post
title: "[Leetcode] 53 Maximum Subarray(Kadane)"
subtitle: ""
categories: algorithm
tags: slidingwindow
comments:
---

## Link: [53 Maximum Subarray(Kadane)](https://leetcode.com/problems/maximum-subarray(kadane)/)

```cpp
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
    int max_sum=INT_MIN;
    int current_sum=0;
    for(int i=0; i<nums.size(); i++){
        current_sum+=nums[i];
        if(current_sum<nums[i]){
            current_sum=nums[i];
        }
        max_sum = max(max_sum,current_sum);
    }
        return max_sum;
    }
};
```
