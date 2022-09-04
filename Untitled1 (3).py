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


# In[1]:


case=1
for i in range(int(input())):
    f=Fals
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


# In[21]:


import itertools
for i in range(int(input())):
    a,b=input().split()
    c=0
    al=[]
    bl=[]
    for i in range(1,len(a)+1):
        x=list(itertools.combinations(a,i))
        for j in x:
            t=''
            for temp in j:
                t+=temp
            al.append(t)
    for i in range(1,len(b)+1):
        x=list(itertools.combinations(b,i))
        for j in x:
            t=''
            for temp in j:
                t+=temp
            for p in al:
                g=p+t
                if g==g[::-1] and len(g)>2:
                    c+=1
                    print(g)
    print(c)


# In[ ]:




