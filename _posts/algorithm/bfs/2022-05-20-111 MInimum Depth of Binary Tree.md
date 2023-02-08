---
layout: post
title: "[Leetcode] 111 MInimum Depth of Binary Tree"
subtitle: ""
categories: algorithm
tags: bfs
comments:
---

## Link: [111 MInimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)

```cpp
class Solution {
public:
    int minDepth(TreeNode* root) {
        if(root==NULL) return 0;
        queue<TreeNode*>Q;
        Q.push(root);
        int depth=0;
        while(!Q.empty()){
            depth++;
            int queueCount=Q.size(); 
            for(int i=0; i<queueCount; i++){
            TreeNode* cur = Q.front();Q.pop();
             if(!cur->left && !cur->right) return depth;
            if(cur->left) Q.push(cur->left);
            if(cur->right) Q.push(cur->right);
            }
        }
        return 0;
    }
};
```
