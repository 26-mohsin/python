#!/usr/bin/env python
# coding: utf-8

# In[ ]:


try :
    sub1 = int(input());
    sub2 = int(input());
    sub3 = int(input());
    sub4 = int(input());
    sub5 = int(input());
    addnum = sub1+sub2+sub3+sub4+sub5;
    average = addnum/5;
    if(average>=91 and average<=100):
        print("Your Grade is A");
    elif(average>=71 and average<=80):
        print("Your Grade is B");
    elif(average>=41 and average<=50):
        print("Your Grade is C");
    elif(average>=0 and average<=40):
        print("Your Grade is F");
    else:
        print("Tum se na hopyga ha ha!");
except:
         print("Sorry Correct The Value")


# In[ ]:




