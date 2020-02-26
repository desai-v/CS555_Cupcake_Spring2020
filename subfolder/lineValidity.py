# Function to check the validity of the line in GEDCOM file


def isvalid(parser):
    lvlonetags = ('NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', "MARR", 'HUSB', 'WIFE', 'CHIL', 'DIV')
    lvlzero = ('HEAD', "TRLR", 'NOTE')
    lvlidentity = ('FAM', 'INDI')
    lvltwotags = 'DATE'

    level = parser[0]
    tag = parser[1]
    val = 'N'
    args = ' '.join(parser[2:])
    # check for tag IND or FAM separately
    if level == '0' and parser[1] in lvlzero:
        val = 'Y'
    elif level == '0' and parser[2] in lvlidentity:
        tag = parser[2]
        args = parser[1]
        val = 'Y'
    elif level == '1' and parser[1] in lvlonetags:
        val = 'Y'
    elif level == '2' and parser[1] in lvltwotags:
        val = 'Y'
    # end of else
    if val == 'N':
        return None
    else:
        # returns a list
        return level, tag, args
