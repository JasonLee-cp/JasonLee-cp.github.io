---
layout: post
title: "[Leetcode] 746 Min Cost Climbing Stairs"
subtitle: ""
categories: algorithm
tags: dp
comments:
---

## Link: [746 Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/)

```cpp
class Solution {
public:
    int dp[1001]{};
    vector<int> v;
    int topdown(int n){
        if(n==0 || n==1) return 0;
        if(dp[n]) return dp[n];
        dp[n]=min(v[n-1]+topdown(n-1), v[n-2]+topdown(n-2));
        return dp[n];
    }
    int minCostClimbingStairs(vector<int>& cost) {
        v = cost;
        return topdown(cost.size());
    }
};
```
