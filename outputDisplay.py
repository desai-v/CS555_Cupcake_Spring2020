# import pretty table for displaying output in Prettytable format


def outputtable(indi, fam):
    import prettytable
    import datetime

    itable = prettytable.PrettyTable()
    # adding fieldnames
    itable.field_names = ["ID", "NAME", "GENDER", "BIRTHDAY", "AGE", "ALIVE", "DEATH", "CHILD", "SPOUSE"]

    # adding rows to the table
    for item in indi:
        newrow = [item["INDI"],
                  item["NAME"],
                  item["SEX"],
                  item["BIRT"] if item["BIRT"] == "NA" else item["BIRT"].strftime("%d %b %Y"),
                  calculateage(item["BIRT"], item["DEAT"]),
                  "TRUE" if item["DEAT"] == "NA" else "FALSE",
                  item["DEAT"] if item["DEAT"] == "NA" else item["DEAT"].strftime("%d %b %Y"),
                  str(item["FAMC"]),
                  str(item["FAMS"])]
        itable.add_row(newrow)

    # printing the table
    print(itable)
    # creating text file
    newf = open('Output_Project.txt', 'w')
    newf.write(str(itable))
    newf.write("\n")

    ftable = prettytable.PrettyTable()
    # adding fieldnames
    ftable.field_names = ["ID", "MARRIED", "DIVORCED", "HUSBAND ID", "HUSBAND NAME", "WIFE ID", "WIFE NAME", "CHILDREN"]

    # adding data
    for item in fam:
        husbobj = dictsearch(item["HUSB"], indi)
        wifeobj = dictsearch(item["WIFE"], indi)
        newrow = [item["FAM"],
                  item["MARR"] if item["MARR"] == "NA" else item["MARR"].strftime("%d %b %Y"),
                  item["DIV"] if item["DIV"] == "NA" else item["DIV"].strftime("%d %b %Y"),
                  item["HUSB"],
                  "NA" if husbobj is None else husbobj["NAME"],
                  item["WIFE"],
                  "NA" if wifeobj is None else wifeobj["NAME"],
                  str(item["CHIL"])]
        ftable.add_row(newrow)

    # printing the table
    print(ftable)
    # adding table to text file
    newf.write(str(ftable))
    newf.close()


# calculateage function referred from https://www.geeksforgeeks.org/python-program-to-calculate-age-in-year/


def calculateage(birth, death):
    from datetime import date
    latest = date.today()
    if death != "NA":
        latest = death.date()

    days_in_year = 365.2425
    age = int((latest - birth.date()).days / days_in_year)
    return str(age)


def dictsearch(uid, itemlist):
    for i in itemlist:
        if i["INDI"] == uid:
            return i
