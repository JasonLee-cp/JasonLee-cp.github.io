---
layout: post
title: "[Leetcode] 102 Binary Tree Level Order Traversal"
subtitle: ""
categories: algorithm
tags: bfs
comments:
---

## Link: [102 Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)

```cpp

class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        if(!root) return {};
        queue<TreeNode*>Q;
        vector<vector<int>> res;
        Q.push(root);
        int cnt=0;
        while(!Q.empty()){
            int size = Q.size();
            res.push_back({});
            while(size--){
                auto cur = Q.front(); Q.pop();
                res[cnt].push_back(cur->val);
                if(cur->left) Q.push(cur->left);
                if(cur->right) Q.push(cur->right);
            } cnt++;
        }
        return res; 
    }
};
```
