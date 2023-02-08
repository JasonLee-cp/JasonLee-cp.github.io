---
layout: post
title: "[Leetcode] 392 Is Subsequence"
subtitle: ""
categories: algorithm
tags: dp
comments:
---

## Link: [392 Is Subsequence](https://leetcode.com/problems/is-subsequence/)

```cpp
class Solution {
public:
    bool isSubsequence(string s, string t) {
        int i=0, j=0;
        while(j<t.length()){
            if(t[j]==s[i])i++;
            j++;
        }
        cout<<i<<" "<<j;
        if(i<s.length()) return false;
        return true;
    }
};
```
