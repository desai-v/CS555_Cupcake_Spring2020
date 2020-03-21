from datetime import datetime


def us04(indi, fam, f):
    print("User Story 4: Marriage before divorce")
    for person in indi:
        m = person['MARR']
        n = person['DIV']

        if m > n:
            print(f"ERROR: {person['INDI']} {person['NAME']} had divorced before marriage")
        elif m < n:
            print(f"{person['INDI']} {person['NAME']} married before divorce")
        else:
            print(f"{person['INDI']} {person['NAME']} married and divorced on same date") 

    print("User Story 4 Completed")
    return True

# Divorce before death
#User Story 6: Divorce before death
def us06(indi, fam, f):
    print("User Story 4: Divorce before death")
    for person in indi:
        m = person['DEAT']
        n = person['DIV']

        if m != None and n!= None:
            if m > n:
                print(f"{person['INDI']} {person['NAME']} had divorced before they died")
            else:
                print(f"ERROR: {person['INDI']} {person['NAME']} died before they divorced")
        if m!= None and n == None:
            print(f"{person['INDI']} {person['NAME']} died but was not divorced")
        if m == None and n!= None:
            print(f"{person['INDI']} {person['NAME']} has divorced but not died")

    print("User Story 4 Completed")
    return true


# Birth before death
from subscripts.outputDisplay import calculateage


def us03(indi, fam, f):
    flag = True
    print("User Story 03 - Birth before death, Running")
    for person in indi:
        m = person['DEAT']
        if person['DEAT'] == 'NA':
            m = datetime.now()

        if person['BIRT'] > m:
            print(f"Error: INDIVIDUAL: US03: {person['INDI']} {person['NAME']} were born before they died")
            f.write(f"Error: INDIVIDUAL: US03: {person['INDI']} {person['NAME']} were born before they died \n")
            flag = False

    print("User Story 03 Completed")
    return flag


# Birth before marriage of parent
def us08(indi, fam, f):
    flag = True
    print("User Story 08 - Birth before marriage of parent, Running")
    for family in fam:
        marriagedate = family["MARR"]
        if family["CHIL"] is "NA":
            continue
        for child in family["CHIL"]:
            childobj = next((item for item in indi if item["INDI"] == child), False)

            if childobj and childobj["BIRT"] > marriagedate:
                if family["DIV"] != "NA" and childobj["BIRT"] > family["DIV"] + timedelta(days=273.93188):
                    print(
                        f" Error: INDIVIDUAL: US08: id -> {childobj['INDI']}, Birth 9 months after divorce of parents")
                    f.write(
                        f"Error: INDIVIDUAL: US08: id -> {childobj['INDI']}, Birth 9 months after divorce of "f"parents \n")
                    flag = False
                continue
            elif childobj["BIRT"] < marriagedate:
                print(f"Error: INDIVIDUAL: US08: id -> {childobj['INDI']}, Birth before marriage of parents")
                f.write(f"Error: INDIVIDUAL: US08: -> {childobj['INDI']}, Birth before marriage of parents \n")
                flag = False
            else:
                print(f'Error: INDIVIDUAL: US08: child with id {child} does not exist in indi list')
                f.write(f"Error: INDIVIDUAL: US08:child with id {child} does not exist in indi list \n")
                flag = False

    print("User Story 08 Completed")
    return flag


