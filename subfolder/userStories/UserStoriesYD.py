

from datetime import date
from datetime import datetime

# User Story 5 - Marriage before death
def us5(indi,fam):
    print("User Story 5 Started")
    for j in fam:
        for i in indi:
            marriage=j["MARR"]
            death=i["DEAT"]
            if i['DEAT'] == 'NA':
                death = datetime.now()
            if(marriage < death):
                pass
    print("User Story 5 Completed")
    return True

# User Story 12 - Parents not too old
def us12(indi,fam):
    
    print("User Story 12 started")
    for j in fam:
        for i in indi:
            if i["INDI"] == j["WIFE"]:
                agemom=i["BIRT"].date()
             
                if i["BIRT"]=="NA":
                    pass
                for child in j["CHIL"]:
                    childobj = next((item for item in indi if item["INDI"] == child), False)
                    agechild=childobj["BIRT"].date()
                    
                days = 365.2425
                age=((agemom-agechild).days/days)
              
                if age < 60:
                    pass
                else:
                    print(" mother too old  ")
                    
           
            if i["INDI"] == j["HUSB"]:
                agehusb=i["BIRT"].date()
             
                if i["BIRT"]=="NA":
                    pass
                for child in j["CHIL"]:
                    childobj = next((item for item in indi if item["INDI"] == child), False)
                    agechild=childobj["BIRT"].date()
                    
                days = 365.2425
                age=((agehusb-agechild).days/days)
              
                if age < 60:
                    pass
                else:
                    print(" father too old  ")
                    
    print("User Story 12 Completed")
    return True