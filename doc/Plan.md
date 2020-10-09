*Replace the bold text with your own content*

*Adapted from https://htdp.org/2020-5-6/Book/part_preface.html*

# 0.  From Problem Analysis to Data Definitions
 The program is going to take a the large CSV file and calculate the economy report of the different areas. 
 Sepcifically It will give the total annual wages, number of establisments, and the employment level.
 It will also give the max wage, max establishment, and max employment level along with the locations of 
 these places. It will also print a specific software industry report very similar to the total economy report
 but this time only dealing with software. It will also give the number of FIPS areas in the report.



# 1.  System Analysis
Open two large CSV file and then turn the contents into a python dictionary. 
Both files will be in the same directory.

Need to learn how to use split better to only split on one comma. and then be able to remove quotes from 
the output. 

remove overlapping AreaFIPS. there is going to be an easy way to do this. ->study the document online of 
areafips naming. remove trailing 000 areas

This is kind of like cut, might need to review the concepts of it to pull the information out of the singlefile.

I need to search the file and get the FIPS to make sure it is not "XX000" then I need to search for either
a "0","10" for the totals or a "5","5112" for the software. This will give me all the data that I need from the file. 
I will need to convert the three values I need into an integer. Then I will need to save the max value and its FIPS
of each of the three values.

I will need to count the number of FIPS that I use and keep the software separate from the totals.

I will need a dictionary with the FIPS mapped to the name. 

ways to determine which FIPS I want to read:
    isdigit: will remove any CSA, MSA, MicroSA, U.S COmbined, and TOTAL areas
    XX000: will remove any statewide and FBI areas



# 2.  Functional Examples
def main():
    open areaTitle
    map area code to name
    close the file
    open singlefile
    for all lines in file
        pull FIPS from line
        if FIPS isdigit and doesn't have three 0's
            pull job codes
            if job codes 0 and 10
                pull Total wage, estab, and employ
                turn into integers
                add 1 to total count
                add wage to total wage
                add esab to total estab
                add employ to total employ
                if max wage < wage 
                    replace
                if max estab < estab
                    replace
                if max employ < employ
                    replace
            else if job codes 5 and 5112
                same as above but for software
            else: 
                continue
        else 
            continue
    give report object the needed information
    close the file

def pull(line, desiredColumn):
    split line by ,
    access the correct location
    remove "
    return infoInColumn (string)

# 3.  Function Template

/* main: will open the files and then find the needed information. it will then give the
* inforamtion to a report object and let it print it out.
*/

/* pull: will pull the needed information out of a line given to it.*/

# 4.  Implementation

Completed implementation

# 5.  Testing

need to verify that I am allowed to use owncode and industrycode and that it won't 
affect the contrived data results. Currently my code works for the given inputs.

python src/main.py data/DC_combined
    output should match exactly DC_combined/output.txt

can do all other tests in data

Note: DE_* has many zeros in it and so to make sure it still works we need to make 
    sure that we only check for the last three digits of the FIPS being zeros. not 
    that there are three zeros in it. 
