---
layout: post
title: "[Leetcode] 279 Perfect Squares"
subtitle: ""
categories: algorithm
tags: dp
comments:
---

## Link: [279 Perfect Squares](https://leetcode.com/problems/perfect-squares/)

```cpp
class Solution {
public:
   
    int numSquares(int n) {
      vector<int>dp(n+1,n+1);
        dp[0]=0;
        for(int i=1; i<=n; i++){
            for(int j=1; j*j<=i; j++){
                dp[i]=min(dp[i],1+dp[i-j*j]);
            }
        }
        return dp[n];
    }
};
```
