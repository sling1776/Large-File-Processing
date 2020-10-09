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
areafips naming.

This is kind of like cut, might need to review the concepts of it to pull the information out of the singlefile.

I need to search the file and get the FIPS to make sure it is not "XX000" then I need to search for either
a "0","10" for the totals or a "5","5112" for the software. This will give me all the data that I need from the file. 
I will need to convert the three values I need into an integer. Then I will need to save the max value and its FIPS
of each of the three values.

I will need to count the number of FIPS that I use and keep the software separate from the totals.

I will need a dictionary with the FIPS mapped to the name. 
I should probably save a second dictionary with the FIPS mapped to a list of the desired numbers. 

# 2.  Functional Examples

**Design a process for obtaining the output from the input.  Consider both *good*
and *bad* inputs.  Find or create examples of both kinds of input.**

**Work out problem examples on paper, on a whiteboard or some other medium that
is *not* your computer.  It is a mistake to begin writing executable code
before you thoroughly understand what form the algorithm(s) must take.**

**Instead, describe components of the system in *"pseudocode"*.  Expect to make
lots of mistakes at this point.  You will find that it is much easier to throw
away pseudocode than real code.**

**Manually work through several examples that illustrate the program's overall
purpose, as well as the purpose of each component of the finished system.  You
will converge on a correct solution much faster if you feel comfortable making
mistakes as you go.**

**This phase involves the use of many levels of abstraction to decompose the
problem into manageable components, and design strategies for implementing each
component.  Components may be functions, modules or classes.**


# 3.  Function Template

**Combine the function stubs written in step #2 with pseudocode from step #3.
Comment out the pseudocode, leaving a valid program that compiles/runs without
errors.  At this stage your program doesn't quite work, but it also doesn't
crash.**


# 4.  Implementation

**This is the only part of the process focused on writing code in your chosen
programming language.**

**One by one translate passages of pseudocode into valid code.  Fill in the gaps
in the function template.  Exploit the purpose statement and the examples.**

**If you were thorough in the previous steps and are familiar with your
programming system this part will go by very quickly and the code will write
itself.**

**When you are learning a new programming language or an unfamiliar library this
phase can be slow and difficult.  As you gain experience with the relevant
technologies you will spend less and less time in this phase of the process.**


# 5.  Testing

**Articulate the examples given in step #2 as tests and ensure that each
function passes all of its tests.  Doing so discovers mistakes.  Tests also
supplement examples in that they help others read and understand the definition
when the need arises—and it will arise for any serious program.**

**As bugs are discovered and fixed, devise new test cases that will detect these
problems should they return.**

**If you didn't come across any bugs (lucky you!) think of a possible flaw and a
test that can be employed to screen for it.**

**At a minimum you should create a document explaining step-by-step how a
non-technical user may manually test your program to satisfy themselves that it
operates correctly.  Explain the entire process starting how to launch the
program, what inputs they should give and what results they should see at every
step.  Provide test cases of good and bad inputs to catch both false positives
and false negatives.  Any deviation from the expected outputs are errors.**

**The ideal is to write an automated test to avoid all manual labor beyond
launching the test.**
