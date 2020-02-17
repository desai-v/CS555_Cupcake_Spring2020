from subfolder.lineValidity import isvalid
from subfolder.parseObjects import inddetails, famdetails
from subfolder.outputDisplay import outputtable


def main() -> None:

    f = open("Project01_Cupcake.ged", "r")

    obj = None 
    currtag = None 
    indi = list()  
    fam = list()  

    for line in f:
        elems = line.split()
        v = isvalid(elems)
        if v is None:
            continue

        

        if v[0] is '0' and (v[1] in ('FAM', 'INDI')):
            if currtag is not None:
                if 'INDI' in obj:
                    indi.append(obj)
                else:
                    fam.append(obj)
                obj = None
            
            currtag = v[1]

        elif v[0] is '0':
            # NOTE, TRLR, HEAD
            continue

        
        if currtag == 'FAM':
            obj = famdetails(obj, v)
        elif currtag == 'INDI':
            obj = inddetails(obj, v)
        elif obj is None: 
            currtag = None
    

    
    if 'INDI' in obj:
        indi.append(obj)
    else:
        fam.append(obj)

    f.close()

    
    indi = sorted(indi, key=lambda i: i["INDI"])
    fam = sorted(fam, key=lambda i: i["FAM"])

    
    outputtable(indi, fam)

   


if __name__ == "__main__":
    main()