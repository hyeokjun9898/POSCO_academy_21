#!/usr/bin/env python
# coding: utf-8

# In[32]:


from collections import deque
# import sys
# sys.stdin = open("input2.txt","r")
# input = sys.stdin.readline
t = int(input())
# t = int(input().rstrip())
for _ in range(t):
    q = deque([])
    a = list(input().split())
    for i in range(len(a)):
#         if a[i] not in q: # 입력 값을 차례대로 넣기
        q.append(a[i])
            
        if len(q) >1 and q[0] == a[i]: # q첫번째와 같다면 빼기, 아니면 False
            q.popleft()
            q.pop()

    if len(q) == 0:
        print("NO")
    else:
        print("YES")
            


# In[ ]:




