from datetime import datetime
from datetime import timedelta
from subscripts.userStories.UserStoriesDP import getIndiByID, getFamByID
from subscripts.userStories.UserStoriesVD import getAgeById


# Birth before Marriage
def us02(indi, fam, f):
    print("User Story 2 - Birth before Marriage, Running")
    # SETTING 8
    flag = True
    for families in fam:
        for person in indi:
            if families['HUSB'] == person['INDI'] or families['WIFE'] == person['INDI']:
                # CHECK IF PERSON HAS BIRTHDATE
                if person['BIRT'] == 'NA':
                    print("NO BIRTHDATE FOUND")
                    f.write(
                        f"Error: INDIVIDUAL: US02: {person['INDI']} {person['NAME']} birthdate not found \n")
                    flag = False
                # SETTING M = BIRTHDATE
                m = person['BIRT']
                # COMPARING MARRIAGE DATE TO BIRTHDATE
                if families['MARR'] < m:
                    print(
                        f" User Story 02  Error: {person['INDI']} {person['NAME']} was born before marriage")
                    f.write(
                        f"Error: INDIVIDUAL: US02: {person['INDI']} {person['NAME']} was born before marriage\n")
                    flag = False
    if flag:
        print("User Story 2 Completed")
        return True
    else:
        return False


# Birth before death of parents


def us09(indi, fam, f):
    print("User Story 9 - Birth before death of parents, Running")
    # SETTING FLAG
    flag = True
    for family in fam:
        fatherdeath = 'NA'
        motherdeath = 'NA'
        # CHECKING FOR DEATH DATES OF MOTHER AND FATHER
        for person in indi:
            if family["HUSB"] == person["INDI"]:
                if person["DEAT"] != 'NA':
                    fatherdeath = person["DEAT"] + timedelta(weeks=36)

            if family["WIFE"] == person["INDI"]:
                if person["DEAT"] != 'NA':
                    motherdeath = person["DEAT"]
        if family["CHIL"] != 'NA':
            for child in family["CHIL"]:
                childobj = next(
                    (item for item in indi if item["INDI"] == child), False)
                if childobj != "NA":
                    if fatherdeath != "NA":
                        # checking if child is born after death of parents
                        if childobj["BIRT"] > fatherdeath:
                            print(
                                f"Indi id -> {childobj['INDI']}, Birth after death of parents")
                            f.write(
                                f"Error: INDIVIDUAL: US09: {childobj['INDI']} {childobj['NAME']} Birth after death of parents  \n")
                            flag = False
                    if motherdeath != "NA":
                        if childobj["BIRT"] > motherdeath:
                            print(
                                f"Indi id -> {childobj['INDI']}, Birth after death of parents")
                            f.write(
                                f"Error: INDIVIDUAL: US09: {childobj['INDI']} {childobj['NAME']} Birth after death of parents  \n")
                            flag = False
    if flag:
        print("User Story 9 Completed")
        return True
    else:
        return False


# Parents should not be too old User Story 12

def us12(indi, fam, f):
    print("User Story 12 - Parents  not too old , Running")
    flag = True
    for family in fam:
        fatherbirth = 'NA'
        motherbirth = 'NA'
        # CHECKING FOR BIRTH DATES OF MOTHER AND FATHER
        for person in indi:
            if family["HUSB"] == person["INDI"]:
                if person["BIRT"] != 'NA':
                    fatherbirth = person["BIRT"] + timedelta(weeks=4171.43)
            if family["WIFE"] == person["INDI"]:
                if person["BIRT"] != 'NA':
                    motherbirth = person["BIRT"] + timedelta(weeks=3128.57)
        if family["CHIL"] != 'NA':
            for child in family["CHIL"]:
                childobj = next(
                    (item for item in indi if item["INDI"] == child), False)
                if childobj != "NA" and fatherbirth != "NA" and motherbirth != "NA":
                    # checking if child is born after death of parents
                    if childobj["BIRT"] > motherbirth or childobj["BIRT"] > fatherbirth:
                        print(
                            f"Indi id -> {childobj['INDI']}, Parents are too old")
                        f.write(
                            f"Error: INDIVIDUAL: US12: {childobj['INDI']} {childobj['NAME']} Parents are too old\n")
                        flag = False
    if flag:
        print("User Story 9 Completed")
        return True
    else:
        return False


def us19(indi, fam, f):
    flag = True
    print("User Story 19 - First cousins should not marry, running")
    for family in fam:
        grandfatherfamc = 0
        grandmotherfamc = 1
        husband = getIndiByID(indi, family["HUSB"])  # Getting Husband Data
        if husband["FAMC"] != 'NA':
            husbandfamc = getFamByID(fam, husband["FAMC"][0])
            # Getting Husband family child id
            if husbandfamc["HUSB"] != 'NA':
                grandfather = getIndiByID(indi, husbandfamc["HUSB"])
                # Comparing family id of paternal grandfather
                if grandfather["FAMC"] != 'NA':
                    grandfatherfamc = getFamByID(fam, grandfather["FAMC"][0])
                else:
                    # if match not found setting random value
                    grandfatherfamc = 0
            if husbandfamc["WIFE"] != 'NA':
                grandmother = getIndiByID(indi, husbandfamc["WIFE"])
                if grandmother["FAMC"] != 'NA':
                    grandmotherfamc = getFamByID(fam, grandmother["FAMC"][0])
                else:
                    # if match not found setting random value
                    grandmotherfamc = 1
        wife = getIndiByID(indi, family["WIFE"])
        if wife["FAMC"] != 'NA':
            wifefamc = getFamByID(fam, wife["FAMC"][0])
            # Comparing family id of maternal grandfather
            if wifefamc["HUSB"] != 'NA':
                wgrandfather = getIndiByID(indi, wifefamc["HUSB"])
                if wgrandfather["FAMC"] != 'NA':
                    wgrandfatherfamc = getFamByID(fam, wgrandfather["FAMC"][0])
                else:
                    # if match not found setting random value
                    wgrandfatherfamc = 2
            if wifefamc["WIFE"] != 'NA':
                wgrandmother = getIndiByID(indi, wifefamc["WIFE"])
                if wgrandmother["FAMC"] != 'NA':
                    wgrandmotherfamc = getFamByID(fam, wgrandmother["FAMC"][0])
                else:
                    # if match not found setting random value
                    wgrandmotherfamc = 3
            # Preventing the case if siblings are married
            if wife["FAMC"] != husband["FAMC"]:
                if wgrandfatherfamc == grandfatherfamc or wgrandfatherfamc == grandmotherfamc or wgrandmotherfamc == grandmotherfamc or wgrandmotherfamc == grandfatherfamc:
                    print(f'Error: FAMILY: US19: spouses {family["HUSB"]} and {family["WIFE"]} are first cousins')
                    f.write(f'Error: FAMILY: US19: spouses {family["HUSB"]} and {family["WIFE"]} are first cousins\n')
                    flag = False

    print("User Story 19 Completed")
    return flag


