
from subscripts.lineValidity import isvalid
from subscripts.objectValidity import objectvalid
from subscripts.parseFile import fileParser
from subscripts.outputDisplay import outputtable


def main() -> None:
    # please select the file by inserting name here
    # filename = "Project01.ged"

    filename = "sprint_02.ged"
    gedcom_list = fileParser(filename)

    # print the table and output a text file
    outputtable(gedcom_list[0], gedcom_list[1])

    # run user story functions inside this function
    objectvalid(gedcom_list[0], gedcom_list[1], gedcom_list[2])


if __name__ == "__main__":
    main()
