#!/usr/bin/env python
# coding: utf-8

# In[1]:


case=1
for i in range(int(input())):
    a=[int(i) for i in input().split()]
    if sum(a)%3==0:
        print(f"Case {case}: Peaceful")
    else:
        print(f"Case {case}: Fight")
    case+=1


# In[8]:


case=1
for i in range(int(input())):
    f=False
    a=[int(i) for i in input().split()]
    k=a.pop()
    b=[abs(a[0]-a[1]),abs(a[1]-a[2]),abs(a[0]-a[2])]
    for j in b:
        if j%k==0:
            f=True
        else:
            f=False
    if f and (sum(a)//3)%k==0:
        print(f'Case {case}: Peaceful')
    else:
        print(f'Case {case}: Fight')


# In[ ]:




