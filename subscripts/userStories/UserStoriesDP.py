from datetime import datetime
from datetime import timedelta
from subscripts.outputDisplay import calculateage

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

# Divorce before death
def us06(indi, fam, f):
    print("User Story 6 - Divorce before death, Running")
    flag = True
    for families in fam:
        for individuals in indi:
            # checking for husband id is equal to individual id
            if families['HUSB'] == individuals['INDI']:
                # getting death date for husband's individual
                m = individuals['DEAT']
                # If individual's death date is not null and families divorce date is not null
                if m != 'NA' and families['DIV'] != 'NA':
                    # checking for husband's death date less than the divorces date
                    if m < families['DIV']:
                        f.write(
                            f"ERROR: FAMILY : US06 : {individuals['INDI']} : Divorced {families['DIV']} after husband's ({individuals['INDI']}) death on {individuals['DEAT']} \n")
                        flag = False

            # checking for wife id is equal to individual id
            if families['WIFE'] == individuals['INDI']:
                # getting death date for wifi's individual
                n = individuals['DEAT']
                # If individual's death date is not null and families divorce date is not null
                if n != 'NA' and families['DIV'] != 'NA':
                    # checking for wife's death date less than the divorces date
                    if n < families['DIV']:
                        f.write(
                            f"ERROR: FAMILY : US06 : {individuals['INDI']} : Divorced {families['DIV']} after wifi's ({individuals['INDI']}) death on {individuals['DEAT']} \n")
                        flag = False

    print("User Story 6 Completed")
    return flag

# Marriage before divorce
def us04(indi, fam, f):
    flag = True
    print("User Story 4 - Marriage before divorce, Running")
    for family in fam:
        # Gets divorce date of family
        div = family['DIV']

        # If family has no divorce date then continue
        if div == 'NA':
            continue
        # If div date exists then
        else:
            marr = family['MARR']
            if marr == 'NA':
                print(
                    f"No marraiage date found in family with id {family['FAM']}")

            if div < marr:
                print(
                    f"FAMILY: us04: {family['FAM']}: divorce {family['DIV']} before marriage {family['MARR']} ")
                f.write(
                    f"ERROR: FAMILY: us04: {family['FAM']}: divorce {family['DIV']} before marriage {family['MARR']} \n")
                flag = False

    # end of for loop
    if flag:
        print("User Story 4 Completed")
        return True
    else:
        print("User Story 4 Completed")
        return False


# helper function 1
def getIndiByID(indi, iD):
    return next((dictionary for dictionary in indi if dictionary['INDI'] == iD), None)


# helper function 2
def getFamByID(fam, iD):
    return next((dictionary for dictionary in fam if dictionary["FAM"] == iD), None)
