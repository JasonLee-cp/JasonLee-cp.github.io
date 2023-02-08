---
layout: post
title: "[Leetcode] 77 Combinations"
subtitle: ""
categories: algorithm
tags: backtracking
comments:
---

## Link: [77 Combinations](https://leetcode.com/problems/combinations/)

```cpp
class Solution {
public:
    vector<vector<int>> ans;
    int N, M;
    vector<int> res;
    void back(int index, int i){
        if(index==M){
            ans.push_back(res);
            return;
        }
        if(i>N) return;
        res.push_back(i);
        back(index+1,i+1);
        res.pop_back();
        back(index,i+1);
    }
    vector<vector<int>> combine(int n, int k) {
        N=n;
        M=k;
        back(0,1);
        return ans;
    }
};
```
