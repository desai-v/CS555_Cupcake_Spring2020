#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from datetime import date
from datetime import datetime

# User Story 13 - No

def days_between(d1, d2):
    #d1 = datetime.strptime(d1, "%Y-%m-%d")
    #d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)

def usBigamy(indi,fam):
    married = {}
    for j in fam:
        #print(j)
        husb_id , wf_id = j['HUSB'],j['WIFE']
        if husb_id in married or wf_id in married:
            print("Person already married")
            return True
        flag = 0
        id,id1=-1,-1
        for k in indi:
            #print(k)
            if k['INDI'] == husb_id and k['DEAT']=="NA":
                id = flag
            if k['INDI'] == wf_id and k['DEAT'] == "NA":
                id1 = flag
            if id!=-1 and id1!=-1:
                married[indi[id]['INDI']] = indi[id1]['INDI']
                married[indi[id1]['INDI']] = indi[id]['INDI']
            flag = flag + 1
    print("User Story usBigamy completed sucessfully")

def usSibling(indi,fam):
     count=0
     y=2
     for j in fam:
         age=[]
         for child in j["CHIL"]:
             childobj = next((item for item in indi if item["INDI"] == child), False)
             a=childobj["BIRT"].date()
             age.append(a)
         if len(age) < 2:
             continue
         for i in range(len(age)):
             for j in range(i+1,len(age)):
                 b = days_between(age[i],age[j])
                 if b<2 or b>240:
                     print("Difference is less than 2 or grater than 8 months")
     print("User Story usSibling completed sucessfully")
     return True
