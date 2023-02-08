---
layout: post
title: "[Leetcode] 690 Employee Importance"
subtitle: ""
categories: algorithm
tags: bfs
comments:
---

## Link: [690 Employee Importance](https://leetcode.com/problems/employee-importance/)

```cpp
/*
// Definition for Employee.
class Employee {
public:
    int id;
    int importance;
    vector<int> subordinates;
};
*/

class Solution {
public:
    int getImportance(vector<Employee*> employees, int id) {
       unordered_map<int,Employee*>mp;
        for(auto x: employees)
            mp[x->id]=x;
        
        queue<Employee*>Q;
        Q.push(mp[id]);
        int sum=0;
        while(!Q.empty()){
            Employee* cur = Q.front(); Q.pop();
            sum+=cur->importance;
            for(auto sub: cur->subordinates){
                Q.push(mp[sub]);
            }
        }
        return sum;
    }
};
```
