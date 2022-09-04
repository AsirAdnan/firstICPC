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


# In[ ]:




