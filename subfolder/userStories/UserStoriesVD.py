from datetime import date
from datetime import datetime

today = date.today()
dateList = []


# User story 1 - all dates should be before current date
def DatebeforeCurrentDate(indi, fam):
    print("User story 1 - All dates should be before current date")
    print(" ")
    for i in indi:
        # Checking death dates are before current dates and NA
        if str(i["DEAT"]) == "NA":
            pass
        elif i["DEAT"].date() > today:
            print(" Wrong death dates ")

        # Checking for Birth dates are before current Date
        if str(i["BIRT"]) == "NA":
            pass
        elif i["BIRT"].date() > today:
            print(" These dates are after the current date: " + str(i["NAME"]) + str(i["BIRT"].date()))

    for j in fam:

        if j["MARR"].date() > today:
            print(" Marriage date " + str(j["MARR"].date()) + " cannot be after current date " + str(today))

        if str(j["DIV"]) == "NA":
            pass
        elif j["DIV"].date() > today:
            print(" Divorce date " + str(j["DIV"].date()) +" cannot be after the current date " + str(today))
    print(" ")
    print(" User stroy 1 ends ")
    print(" ")
    

# User story 10 - Marriage should be after 14 years of age
def MarriageAfter14(indi, fam):
    print("User story 10 - Marriage should be after 14 years of age")
    print(" ")
    for j in fam:
        for i in indi:
            if i["INDI"] == j["WIFE"]:
                days = 365.2425
                age = int(((j["MARR"].date()) - (i["BIRT"].date())).days / days)
                if age > 14:
                    pass
                else:
                    print("Invalid marriage date ")

            if i["INDI"] == j["HUSB"]:
                days = 365.2425
                age = int(((j["MARR"].date()) - (i["BIRT"].date())).days / days)
                if age > 14:
                    pass
                else:
                    print(" Invalid marriage date ")                 
    print(" ")
    print(" User story 10 Completed ")
    print(" ")
