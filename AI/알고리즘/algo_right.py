#!/usr/bin/env python
# coding: utf-8

# In[13]:


# import sys
# sys.stdin = open("input.txt","r")
# input = sys.stdin.readline
t = int(input())
# t = int(input().rstrip())
for _ in range(t):
    bracket = input()
#     bracket = input().rstrip()
    stk = [] #스택 초기화
    correct = True #올바른 괄호열인지 저장하는 변수
    for b in bracket:
        if b =="(" or b =="{" or b =="[":   #여는 괄호의 경우, 스택에 넣음
            stk.append(b)
        elif len(stk) == 0 :#스택이 비어있거나, pop된 괄호와 매칭 x인 경우
            correct = False
            break
        elif b == ")":
            if stk.pop() != "(":
                correct = False
                break
        elif b == "}":
            if stk.pop() != "{":
                correct = False
                break
        elif b == "]":
            if stk.pop() != "[":
                correct = False
                break
    if len(stk) !=0: #괄호열이 끝났는데, 닫혀지지 않은 괄호가 남은 경우
        correct = False
    if correct == True:
        print("YES")
    else:
        print("NO")


# In[ ]:




