from datetime import date
from subscripts.outputDisplay import calculateage


today = date.today()
dateList = []


# User story 1 - all dates should be before current date
def us01(indi, fam , f):
    print("US 01 - all dates should be before current date, Running")
    lag = True 
    for i in indi:
        # Checking death dates are before current dates and NA
        if str(i["DEAT"]) == "NA":
            pass
        elif i["DEAT"].date() > today:
            print("US 01 Error indi id ->" + str(i["INDI"]) + str(i["DEAT"]))
            f.write(f"Error: INDIVIDUAL: US01: Date before Current Date" + str(i["INDI"]) + " "+str(i["DEAT"])+"\n")
            lag =  False

        # Checking for Birth dates are before current Date
        if str(i["BIRT"]) == "NA":
            pass
        elif i["BIRT"].date() > today:
            print("These dates are after the current date: " + str(i["NAME"]) + str(i["BIRT"].date()))
            f.write(f"Error: INDIVIDUAL: US01: Birth date after current date" + str(i["INDI"])+ " "+str(i["NAME"]) +" "+ str(i["BIRT"].date()) +"\n")
            lag = False

    for j in fam:

        if j["MARR"].date() > today:
            print("Error: INDIVIDUAL: US01: Marriage date after current date " + str(j["MARR"].date()) + " " + str(today))
            lag = False
            f.write(f"Error: INDIVIDUAL: US01: Marriage date after current date " + str(j["MARR"].date()) + " " + str(today)+"\n")

        if str(j["DIV"]) == "NA":
            pass
        elif j["DIV"].date() > today:
            print("Error: INDIVIDUAL: US01: Divorce date after current date " + str(j["DIV"].date()) +" " + str(today))
            lag = False
            f.write(f"Error: INDIVIDUAL: US01: Divorce date after current date " + str(j["DIV"].date()) +" " + str(today)+"\n")
    
    if(lag):
        print("US 01 completed")
        return True
    else: 
        return False
    

# User story 10 - Marriage should be after 14 years of age
def us10(indi, fam, f):
    print("US 10 - Marriage should be after 14 years of age, Runnning")
    flag = True
    for j in fam:
        for i in indi:
            if i["INDI"] == j["WIFE"]:
                days = 365.2425
                age = int(((j["MARR"].date()) - (i["BIRT"].date())).days / days)
                if age > 14:
                    pass
                else:
                    print("US 10 Error indi id ->" + str(i["INDI"]) + str(j["MARR"]))
                    f.write("Error: INDIVIDUAL: US10: Too young for marriage " + str(i["INDI"]) +" "+ str(j["MARR"])+"\n")
                    #return False list2.append("false")
                    flag = False

            if i["INDI"] == j["HUSB"]:
                days = 365.2425
                age = int(((j["MARR"].date()) - (i["BIRT"].date())).days / days)
                if age > 14:
                    pass
                else:
                    print("US 10 Error indi id ->" + str(i["INDI"]) + str(j["MARR"])) 
                    f.write("Error: INDIVIDUAL: US10: Too young for marriage " + str(i["INDI"]) +" "+ str(j["MARR"])+"\n")
                    #return False
                      
                    flag = False              
    
    if(flag):
        return True
        print("US 10 completed")
    else:
        return False

# User story 15 - Fewer than 15 siblings
def us15(indi, fam,f):
    print("US 15 - Fewer than 15 sublings - Running")
    flag = True
    list_of_siblings = []
    for i in fam:
        if(len(i["CHIL"]) >= 15):
            list_of_siblings.append(i["FAM"])

    if(len(list_of_siblings) == 0):
        pass
    else:
        print("Error: FAM: US15: More than 15 siblings in a family" + str(i["FAM"]))
        f.write("Error: FAM: US15: More than 15 siblings in a family" + str(i["FAM"])+ "\n")
        flag = False
    if(flag):
        print("US 15 completed")
        return True
    else: return False

#User Story 16


def us16(indi, fam, f):
    print("US 16 - All last names of men in family should be same - Running")
    flag = True
    for j in fam:
        names = []
        names.append(getLastNamebyId(indi, j["HUSB"]))
        if(j["CHIL"] != []):
            for h in j["CHIL"]:
                if(getSexByid(indi, h ) == 'M'):
                    names.append(getLastNamebyId(indi, h))

        if(len(set(names)) != 1):
            print("Error: FAM: US 16: Single family has two or more last name" + str(j["FAM"]))
            f.write("Error: FAM: US 16: Single family has two or more last name " + str(j["FAM"])+"\n")
            flag = False
        elif (len(set(names)) == 1):
            pass

    if(flag):
        return True
        print("US 16 completed")
    else:
        return False


#Helper functions
def getLastNamebyId(indi, Id):
    for i in indi:
        list1= []
        if(i["INDI"] == Id):
            s = i["NAME"]
            #print(s)
            list1 = s.split()
            return list1[1]

def getSexByid(indi, Id):
    sex = ""
    for i in indi:
        if(i["INDI"] == Id):
            sex = i["SEX"]
            
    return sex

def getAgeById(indi, Id):
    age = 0
    for i in indi:
        if(i["INDI"] == Id ):
            age = calculateage(i["BIRT"], i["DEAT"])
    
    return age

def getAliveById(indi, Id):
    alive = True
    for i in indi:
        if(i["DEAT"] == "NA"):
            alive = True
        else: 
            alive = False
    
    return alive

def getNamebyId(indi, Id):
    name = " "
    for i in indi:
        if(i["INDI"] == Id):
            name = i["NAME"]

    return name