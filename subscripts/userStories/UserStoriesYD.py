from datetime import datetime
from subscripts.userStories.UserStoriesDP import getIndiByID, getFamByID


# Marriage before death
def us05(indi, fam, f):
    print("User Story 5 - Marriage before death, Running")
    flag = True
    for families in fam:
        for individuals in indi:
            # checking for husband id is equal to individual id
            if families['HUSB'] == individuals['INDI']:
                # getting death date for husband individual
                m = individuals['DEAT']
                # If individual's death date is not null
                if m != 'NA':
                    # checking for marriage date greater than the individual's death date
                    if families['MARR'] > m:
                        f.write(
                            f"ERROR: INDIVIDUAL : US05 : {individuals['INDI']} : Married {families['MARR']} after husband's ({individuals['INDI']}) death on {individuals['DEAT']} \n")
                        flag = False

            # checking for wife id is equal to individual id
            elif families['WIFE'] == individuals['INDI']:
                # getting death date for wifi individual
                n = individuals['DEAT']
                # If individual's death date is not null
                if n != 'NA':
                    # checking for marriage date greater than the individual's death date
                    if families['MARR'] > n:
                        f.write(
                            f"ERROR: INDIVIDUAL : US05 : {individuals['INDI']} : Married {families['MARR']} after wifi's ({individuals['INDI']}) death on {individuals['DEAT']} \n")
                        flag = False

    print("User Story 5 Completed")
    return flag

# User Story 18, siblings should not marry each other
def us18(indi, fam, f):
    flag = True
    print("User Story 18 - Siblings should not marry each other, running")
    for family in fam:
        husb = getIndiByID(indi, family["HUSB"])
        wife = getIndiByID(indi, family["WIFE"])
        if husb["FAMC"] == wife["FAMC"] and husb["FAMC"] != "NA" and wife["FAMC"] != "NA":
            print(f'Error: FAMILY: US18: spouses {family["HUSB"]} and {family["WIFE"]} are siblings')
            f.write(f'Error: FAMILY: US18: spouses {family["HUSB"]} and {family["WIFE"]} are siblings \n')
            flag = False

    print("User Story 18 Completed")
    return flag


def us20(indi, fam, f):
    print("User Story 20 - Aunts and Uncles should not marry their nieces and nephews , Running")
    flag = True
    for individual in indi:
        if individual["FAMC"] == "NA" or individual["FAMS"] == "NA":
            continue
        # get parents of spouses for an individual
        parents_of_spouses = list()
        spouse_gender = "HUSB"
        if individual["SEX"] == "M":
            spouse_gender = "WIFE"
        for family_id in individual["FAMS"]:
            family = getFamByID(fam, family_id)
            spouse = getIndiByID(indi, family[spouse_gender])
            if spouse["FAMC"] == "NA":
                continue
            else:
                famc_spouse = getFamByID(fam, spouse["FAMC"][0])
                parents_of_spouses.append((spouse["INDI"], famc_spouse["HUSB"]))
                parents_of_spouses.append((spouse["INDI"], famc_spouse["WIFE"]))
        if len(parents_of_spouses) == 0:
            continue

        # for an individual check in "FAMC", if siblings are present as parents of spouses
        famc_individual = getFamByID(fam, individual["FAMC"][0])
        for child in famc_individual["CHIL"]:
            if child == individual["INDI"]:
                continue
            for spouse, parent in parents_of_spouses:
                if child == parent:
                    flag = False
                    print(f"Error: US 20 Individual {spouse} has married their aunt/uncle {individual['INDI']}")
                    f.write(f"Error: US 20 Individual {spouse} has married their aunt/uncle {individual['INDI']}")

    print("User Story 20 Completed")
    return flag
