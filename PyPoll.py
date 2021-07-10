# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

# 4.Declare a new list
candidate_options = []

# 9.Declare an empty dictionary
candidate_votes={}

# 16. Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0



# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
    
    # Print each row in the CSV file.
    for row in file_reader:
        print(row)
        # 2. Add to the total vote count.
        total_votes += 1
        
        # 5. Print the candidate name from each row
        candidate_name = row [2]

        # 8. If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            # 10. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
           
        # 12.Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

     
   
    # 14. Retrieve & covert the candidate votes and total votes
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # 15. candidate name and percentage of votes.
        print(f"{candidate_name}: received {vote_percentage:.2f}% of the vote.")

    # 17. Determine winning vote count and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
        print(f"{candidate_name}, ({votes:,}), {vote_percentage:.1f}%\n")

    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
   
# 3. Print the total votes.
print(total_votes)
# 7. Print the candidate list.  
print(candidate_options)
# 11. Print the candidate votes.
print(candidate_votes)
 
