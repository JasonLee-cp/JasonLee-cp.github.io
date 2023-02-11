---
layout: post
title: "[Leetcode] 64 Minimum Path Sum"
subtitle: ""
categories: algorithm
tags: dp
comments:
---

## Link: [64 Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/)

Hello! Today, we will be looking at a typical DP problem which includes an important DP concept. This question clearly and very intuitively shows how dynamic programming works. As I’ve been trying hard to do so, DO NOT just memorize codes and techniques for interviews but try to understand the thinking process behind the hood.

Problem link: https://leetcode.com/problems/minimum-path-sum/

This question directly and clearly shows conditions of dynamic programming. Rather than memorizing codes, we need to deeply understand why we need DP for this type of question and how we transform our initial thoughts into the actual implementation.

Goal: To find a path with the minimum sum along the way from (0,0) to (n-1,m-1).
Constraints: We can only move down or right on the grid.

## Thinking process

(1) As soon as I read the question, the first thing that came up to my mind is that no matter how we reach the destination `(n-1,m-1)`, we must step on the last cell `(n-1,m-1)`, pretty obviously. This cannot alter.

(2) Then, we need to “somehow” manage to reach the last cell `(n-1,m-1)` with the minimum path sum. The key point is “we don’t care how but we just need to”.

(3) We can only move down or right. In other words, from the perspective of each cell, the previous step must come from either up or left.

(4) Let `dp[i][j] = Minimum path sum required to reach the cell (i,j) from (0,0)`.
-> (Note) Thinking transformation from (3) -> (4) is critical. In this case, it was pretty intuitive but for many other dp questions, it’s not that intuitive and easy to come up with recurrence relation right at a second. It takes time and practice.

(5) Go back to (2) and express this using the recurrence relation from (4).
-> `dp[n-1][m-1] = grid[n-1][m-1] + min(dp[n-2][m-1],dp[n-1][m-2])`

(6) This gives the general recurrence relation.
-> `dp[i][j] = grid[i][j] + min(dp[i-1][j],dp[i][j-1])`
-> `grid[i][j] comes from (1) and min(dp[i-1][j], dp[i][j-1]) comes from (3)`

(7) Base condition: `dp[0][0] = grid[0][0]` since in order to reach `(0,0)` from `(0,0)` we don’t move which would cost `grid[0][0]`.

(8) Out of boundary conditions: when i<0 or j<0 there’s no way to reach there from (0,0) so return INT_MAX since we want to find the minimum path sum. Note that you cannot `dp[i][j] = min(grid[i][j]+dp[i-1][j], grid[i][j]+dp[i][j-1])` since `INT_MAX plus something` would cause an integer overflow. You can either do what I mentioned above or you can carefully compare the input size and set it as, for example, `1e5`.

```cpp
class Solution {
public:

    int minPathSum(vector<vector<int>>& grid) {
        int n = grid.size();
        if(n==0) return 0;
        int m = grid[0].size();
        vector<vector<int>>dp (n,vector<int>(m,INT_MAX));
        dp[0][0]=grid[0][0];
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                if(i==0 && j==0) continue;
                if(i==0) {
                    dp[i][j]=dp[i][j-1]+grid[i][j];
                    continue;
                }
                if(j==0){
                    dp[i][j]=dp[i-1][j]+grid[i][j];
                    continue;
                }
               dp[i][j]=grid[i][j]+min(dp[i-1][j],dp[i][j-1]);
            }
        }
        return dp[n-1][m-1];
    }
};
```
