from datetime import datetime
from datetime import timedelta

# helper function 1
def getIndiByID(indi, iD):
    return next((dictionary for dictionary in indi if dictionary['INDI'] == iD), None)


# helper function 2
def getFamByID(fam, iD):
    return next((dictionary for dictionary in fam if dictionary["FAM"] == iD), None)

def us19(indi, fam, f):
    flag = True
    print("User Story 19 - First cousins should not marry, running")
    for family in fam:
        husband = getIndiByID(indi, family["HUSB"])
        if husband["FAMC"] != 'NA':
            husbandfamc = getFamByID(fam, husband["FAMC"][0])
            if husbandfamc["HUSB"] != 'NA':
                grandfather = getIndiByID(indi, husbandfamc["HUSB"])
                if grandfather["FAMC"] != 'NA':
                    grandfatherfamc = getFamByID(fam, grandfather["FAMC"][0])
                else:
                    grandfatherfamc = 0
            if husbandfamc["WIFE"] != 'NA':
                grandmother = getIndiByID(indi, husbandfamc["WIFE"])
                if grandmother["FAMC"] != 'NA':
                    grandmotherfamc = getFamByID(fam, grandmother["FAMC"][0])
                else:
                    grandmotherfamc = 1
        wife = getIndiByID(indi, family["WIFE"])
        if wife["FAMC"] != 'NA':
            wifefamc = getFamByID(fam, wife["FAMC"][0])
            if wifefamc["HUSB"] != 'NA':
                wgrandfather = getIndiByID(indi, wifefamc["HUSB"])
                if wgrandfather["FAMC"] != 'NA':
                    wgrandfatherfamc = getFamByID(fam, wgrandfather["FAMC"][0])
                else:
                    wgrandfatherfamc = 2
            if wifefamc["WIFE"] != 'NA':
                wgrandmother = getIndiByID(indi, wifefamc["WIFE"])
                if wgrandmother["FAMC"] != 'NA':
                    wgrandmotherfamc = getFamByID(fam, wgrandmother["FAMC"][0])
                else:
                    wgrandmotherfamc = 3

            if wgrandfatherfamc == grandfatherfamc or wgrandfatherfamc == grandmotherfamc or wgrandmotherfamc == grandmotherfamc or wgrandmotherfamc == grandfatherfamc:
                print(f'Error: FAMILY: US19: spouses {family["HUSB"]} and {family["WIFE"]} are first cousins')
                f.write(f'Error: FAMILY: US10: spouses {family["HUSB"]} and {family["WIFE"]} are first cousins')
                flag = False

    print("User Story 19 Completed")
    return flag


def us20(indi,fam,f):
    flag=True
    print("US20 :Aunts and uncles should not marry their nieces or nephews")
    child=[]
    for family in fam:
        child.append(family["CHIL"])
        for ch in child:
            
            if(family["HUSB"]==ch and family["WIFE"]==ch):
                print(f'Error: FAMILY: US20: spouses {family["HUSB"]} and {family["WIFE"]} Aunts and uncles should not marry their nieces or nephews')
                f.write(f'Error: FAMILY: US20: spouses {family["HUSB"]} and {family["WIFE"]} Aunts and uncles should not marry their nieces or nephews')
                flag = False
    print("US20 completed")
    return flag