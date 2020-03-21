from subscripts.lineValidity import isvalid
from subscripts.parseObjects import famdetails, inddetails


def fileParser(filename):
    f = open(filename, "r")

    obj = None  # refers to the actual Dict object being parsed at a given moment
    currtag = None  # The tag being processed currently
    indi = list()  # list of INDI objects
    fam = list()  # list of FAM objects
    us32_ids = list()

    for line in f:
        elems = line.split()
        v = isvalid(elems)  # if line is valid it returns a list of level,tag,args, else returns None
        if v is None:
            # print(f' {line} is invalid')
            continue

        # the line is valid

        if v[0] is '0' and (v[1] in ('FAM', 'INDI')):
            if currtag is not None:
                # add object to correct list
                if 'INDI' in obj:
                    # added us32 code here, because parser already caught the error
                    # changing structure would have lead to refactoring 80% of code
                    if "us32" in obj:
                        us32_ids.append(obj["INDI"])
                        try:
                            obj.pop("us32")
                        except KeyError:
                            print("Key not found")

                    indi.append(obj)
                else:
                    fam.append(obj)
                # end of if
                obj = None
            # set the currtag flag to the new tag being parsed
            currtag = v[1]

        elif v[0] is '0':
            # NOTE, TRLR, HEAD
            continue

        # use currtag to call function to create the appropriate Dict object
        if currtag == 'FAM':
            obj = famdetails(obj, v)
        elif currtag == 'INDI':
            obj = inddetails(obj, v)
        elif obj is None:  # the first valid line is not a FAM or IND
            currtag = None
    # end of for

    # adding the last object in the file
    if 'INDI' in obj:
        indi.append(obj)
    else:
        fam.append(obj)

    f.close()

    # sorting the lists by UID
    indi = sorted(indi, key=lambda i: i["INDI"])
    fam = sorted(fam, key=lambda i: i["FAM"])

    return [indi, fam, us32_ids]
