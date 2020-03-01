from datetime import datetime


# User Story 3 - Birth before death
def us2(indi, fam):
    print("User Story 2 - Birth before death, Running")
    for person in indi:
        m = person['DEAT']
        if person['DEAT'] == 'NA':
            m = datetime.now()

        if person['BIRT'] > m:
            print(f"{person['INDI']} {person['NAME']} were born before they died")

    print("User Story 2 Completed")
    return True


# User Story 8 - Birth before marriage of parent
def us8(indi, fam):
    print("User Story 8 - Birth before marriage of parent, Running")
    for family in fam:
        marriagedate = family["MARR"]
        for child in family["CHIL"]:
            childobj = next((item for item in indi if item["INDI"] == child), False)

            if childobj and childobj["BIRT"] > marriagedate:
                continue
            elif childobj["BIRT"] < marriagedate:
                print(f"Indi id -> {childobj['INDI']}, Birth before marriage")
                return False
            else:
                print(f'child with id {child} does not exist in indi list')
                return False

    print("User Story 8 Completed")
    return True
