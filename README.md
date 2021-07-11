# ELECTION AUDIT

# OVERVIEW
## Purpose
The purpose of this project is to help Tom, a Colorado board of elections employee, to conduct an election audit of the results for US congressional precinct in Colorado. The main information he wants to know, and the tasks that are going to be completed are:

	Obtain the total number of votes cast.
	Obtain the total number of votes for each candidate.
	Obtain the Percentage of votes for each candidate.
	Finally know who Is the winner of the election.
These results are normally obtained with excel, but Toms boss, wants to know if there´s an automated option to do this process using python. If the code is successful and the results are correct, the same python code could be used also for senatorial and local elections.
# ELECTION AUDIT RESULT
### -How many votes were cast in this congressional election?
    The total votes where 369,711
### -Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
    There were 3 counties in the election process, with the next total count of votes and percentages of each one of them:
TOTAL VOTES

    Jefferson: 38,855
    Denver: 306,055
    Arapahoe: 24,801
PERCENTAGES

    Jefferson: 10.5%
    Denver: 82.8%
    Arapahoe: 6.7% 

Running the code, we can see the same results in this summary:

![Title](Resources/county_summary.png)
 
### -Which county had the largest number of votes?

    Accordingly with the below image, the county with the greater number of votes is Denver with 306, 055, representing a 82.8% of the results.
### -Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
    In the election, were 3 candidates, each one of them obtained next total votes and percentages results:

TOTAL VOTES

    Charles Casper Stockham: 85,213
    Diana DeGette: 272,892
    Raymon Anthony Doane: 11,606
PERCENTAGES

    Charles Casper Stockham: 23.0%
    Diana DeGette: 73.8%
    Raymon Anthony Doane: 3.1%
As showed earlier, this results also can be seen as a result of the coding:

![Title](Resources/candidate_summary.png)

 
### -Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

    The election winner is Diana DeGette with 272,892 votes, having a 73.8% of the total results.
# ELECTION AUDIT SUMMARY
## Business Proposal and code reuse
The developed code helps the user to get a summary of the results of an election. In this case, the data were used for a congressional precinct, but basically It can be used with every set of data which information contains counties and candidates.
The code works counting the vote of every county and candidate, in such a way, the program can determine the total number of votes for every candidate_name and county_name: once it get them, the corresponding percentage is easily obtained just dividing the count of votes of the candidate and the total number of votes. To obtain the winner, a comparison is made in order to get the biggest number of votes.
Because the code is not “hard coded” and it uses “for loops” and “if” statements, is simple to reuse it with different sources of data, as soon as they maintain the columns with the candidate, county and ballot information. For example, and as requested, it can be used for senatorial and local elections. 
