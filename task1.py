# TEST DATA - Do not modify
creator_name = "DigitalDreamer"
current_followers = 4567
starting_followers = 2100
days_tracked = 45
milestone_increment = 1000

# YOUR CODE BELOW THIS LINE
# Calculate follower statistics and milestone progress

# Calculate milestone progress
current_milestone = current_followers // milestone_increment

# Calculate growth statistics
progress_in_milestone = current_followers % starting_followers

# Calculate projections
total_gained = current_followers - starting_followers

# Display results with f-strings
daily_average = total_gained // days_tracked

