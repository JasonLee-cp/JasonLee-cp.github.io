---
layout: post
title: "[Leetcode] 107 Binary Tree Level Order Traversal II"
subtitle: ""
categories: algorithm
tags: bfs
comments:
---

## Link: [107 Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)

```cpp
class Solution {
public:
    
  
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        vector<vector<int>>answer;
        if(!root) return answer;
        
        queue<TreeNode*>Q;
        Q.push(root);
        
        while(!Q.empty()){
            int queueCount=Q.size();
            vector<int>bfs;
            while(queueCount>0){
            TreeNode* cur = Q.front(); Q.pop();
            bfs.push_back(cur->val);
            if(cur->left!=NULL) Q.push(cur->left);
            if(cur->right!=NULL) Q.push(cur->right);
                queueCount--;
            } answer.push_back(bfs);
        }   
        
        reverse(answer.begin(),answer.end());
        return answer;
    }
};
```
