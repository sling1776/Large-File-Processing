import time
import sys
from Report import Report
'''
    pull: will pull the needed information out of a line given to it.
        returns a string
'''
def pull(line, desiredColumn):
    info = line.split(",")
    infoInColumn = info[desiredColumn].replace('\"', "")
    return infoInColumn


'''
    main: will open the files and then find the needed information. It will then
        give that information to the report object and let it print it out at the 
        end.
'''

if __name__ == '__main__':
    rpt = Report()
    # Declare Constants
    AREA_FIPS = 0
    OWN_CODE = 1
    INDUSTRY_CODE = 2
    ANNUAL_AVG_ESTABS = 8
    ANNUAL_AVG_EMPLYLVL = 9
    ANNUAL_WAGES = 10

    # if sys.argv[1] is not given, print a usage message and exit
    if len(sys.argv) != 2:
        print("Usage: src/main.py DATA_DIRECTORY")
        sys.exit(1)
    print("Reading the databases...", file=sys.stderr)
    before = time.time()

    # open the file 'sys.argv[1]/area_titles.csv'
    file = open(sys.argv[1] + "/area_titles.csv")

    # Convert the file 'sys.argv[1]/area_titles.csv' into a dictionary
    nameDictionary = {}
    for line in file:
        key, value = line.replace('\"', "").rstrip().split(",", 1)
        nameDictionary[key] = value
    file.close()
    nameDictionary[""] = ""

    # open the file 'sys.argv[1]/2018.annual.singlefile.csv'
    file = open(sys.argv[1] + "/2019.annual.singlefile.csv")
    # Collect information from 'sys.argv[1]/2018.annual.singlefile.csv', place into the Report object rpt
    maxWage = 0
    maxSoftWage = 0
    maxWageFIPS = ""
    maxSoftWageFIPS = ""
    totalWage = 0
    totalSoftWage = 0

    maxEstabs = 0
    maxSoftEstabs = 0
    maxEstabsFIPS = ""
    maxSoftEstabsFIPS = ""
    totalEstabs = 0
    totalSoftEstabs = 0

    maxEmploy = 0
    maxSoftEmploy = 0
    maxEmployFIPS = ""
    maxSoftEmployFIPS = ""
    totalEmploy = 0
    totalSoftEmploy = 0

    FIPSCount = 0
    FIPSSoftCount = 0

    for line in file:
        areaFIPS = pull(line, AREA_FIPS)
        if areaFIPS.isdigit() and (areaFIPS[-3:] != "000"):
            ownCode = pull(line, OWN_CODE)
            indusCode = pull(line, INDUSTRY_CODE)
            if ownCode == "0" and indusCode == "10":
                FIPSCount += 1
                wages = int(pull(line, ANNUAL_WAGES))
                estabs = int(pull(line, ANNUAL_AVG_ESTABS))
                employ = int(pull(line, ANNUAL_AVG_EMPLYLVL))
                totalWage += wages
                totalEstabs += estabs
                totalEmploy += employ
                if wages > maxWage:
                    maxWage = wages
                    maxWageFIPS = areaFIPS
                if estabs > maxEstabs:
                    maxEstabs = estabs
                    maxEstabsFIPS = areaFIPS
                if employ > maxEmploy:
                    maxEmploy = employ
                    maxEmployFIPS = areaFIPS
            if ownCode == "5" and indusCode == "5112":
                FIPSSoftCount += 1
                wagesSoft = int(pull(line, ANNUAL_WAGES))
                estabsSoft = int(pull(line, ANNUAL_AVG_ESTABS))
                employSoft = int(pull(line, ANNUAL_AVG_EMPLYLVL))
                totalSoftWage += wagesSoft
                totalSoftEstabs += estabsSoft
                totalSoftEmploy += employSoft
                if wagesSoft > maxSoftWage:
                    maxSoftWage = wagesSoft
                    maxSoftWageFIPS = areaFIPS
                if estabsSoft > maxSoftEstabs:
                    maxSoftEstabs = estabsSoft
                    maxSoftEstabsFIPS = areaFIPS
                if employSoft > maxSoftEmploy:
                    maxSoftEmploy = employSoft
                    maxSoftEmployFIPS = areaFIPS
            else:
                continue
        else:
            continue
    file.close()


    after = time.time()
    print(f"Done in {after - before:.3f} seconds!", file=sys.stderr)

    # Fill in the report for all industries
    rpt.all.num_areas           = FIPSCount

    rpt.all.total_annual_wages  = totalWage
    rpt.all.max_annual_wage     = (nameDictionary[maxWageFIPS], maxWage)

    rpt.all.total_estab         = totalEstabs
    rpt.all.max_estab           = (nameDictionary[maxEstabsFIPS], maxEstabs)

    rpt.all.total_empl          = totalEmploy
    rpt.all.max_empl            = (nameDictionary[maxEmployFIPS], maxEmploy)


    # Fill in the report for the software publishing industry
    rpt.soft.num_areas          = FIPSSoftCount

    rpt.soft.total_annual_wages = totalSoftWage
    rpt.soft.max_annual_wage    = (nameDictionary[maxSoftWageFIPS], maxSoftWage)

    rpt.soft.total_estab        = totalSoftEstabs
    rpt.soft.max_estab          = (nameDictionary[maxSoftEstabsFIPS], maxSoftEstabs)

    rpt.soft.total_empl         = totalSoftEmploy
    rpt.soft.max_empl           = (nameDictionary[maxSoftEmployFIPS], maxSoftEmploy)


    # Print the completed report
    print(rpt)

