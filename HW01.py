from gedcom.element.individual import IndividualElement


def get_file(path):
    keywords = { '0': ('HEAD', 'NOTE', 'TRLR'),
                 '1': ('BIRT', 'CHIL', 'DEAT', 'DIV', 'FAMC', 'FAMS', 'HUSB', 'NAME', 'SEX', 'WIFE'),
                 '2': ('DATE') }
    filedata = open(path)
    f = open("HW02_Diksha_Pancholi_Output_File.txt", "w")
    output = []
    for data in filedata:
        print(f"--> {data}")
        datawords = data.split(' ')
        if len(datawords) == 3 and datawords[0] == 0 and datawords[2] in ["INDI", "FAM"]:
            level, arguments, tag_data = datawords
            valid = 'Y'
            output.append('<-- {levels}|{tag}|{validity}|{args}'.format(levels = level, tag = tag_data, validity = valid, args = arguments))
            f.write(''.join(output))

        elif len(datawords) >= 2:
            level, tag_data, arguments = datawords[0], datawords[1], " ".join(datawords[2: ])
            valid = 'Y' if level in keywords and tag_data in keywords[level] else 'N'
            output.append('<-- {levels}|{tag}|{validity}|{args}'.format(levels = level, tag = tag_data, validity = valid, args = arguments))
            f.write(''.join(output))
        else:
            level, tag_data, valid, arguments = datawords[0], 'NA', 'N', 'NA'
            output.append('<-- {levels}|{tag}|{validity}|{args}'.format(levels = level, tag = tag_data, validity = valid, args = arguments))
            f.write(''.join(output))

        print(f"<-- {level}|{tag_data}|{valid}|{arguments}")
            
    f.close()
        

if __name__ == '__main__':
    file_path = 'D:\SEM 4\Agile Methodology\Assignments\Project01_Diksha_Pancholi.ged'
    get_file(file_path)

