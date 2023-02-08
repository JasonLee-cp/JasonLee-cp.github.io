---
layout: post
title: "[Leetcode] 46 Permutations"
subtitle: ""
categories: algorithm
tags: backtracking
comments:
---

## Link: [46 Permutations](https://leetcode.com/problems/permutations/)

```cpp
class Solution {
public:
    int n;
    vector<bool>vis;
    vector<int>res;
    vector<vector<int>> ans;
    void backtracking(vector<int> nums, int k){
        if(k==n){
            ans.push_back(res);
            return;
        }
        
        for(int i=0; i<n; i++){
            if(vis[i]) continue;
            res[k]=nums[i];
            vis[i]=true;
            backtracking(nums,k+1);
            vis[i]=false;
        }
    }
    vector<vector<int>> permute(vector<int>& nums) {
        n = nums.size();
        vis = vector<bool>(n,0);
        res = vector<int>(n);
        backtracking(nums,0);
        return ans;
        
    }
};
```
