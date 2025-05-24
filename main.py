# Yvonne Richardson
# STEM 103
# 05-18-2025

# Level 2: Program with For Loops
    
# This program analyzes data from a list of space missions. Each mission has information 
# about its name, year, and success status. A for loop is used to process this data and
# extract useful information.

# The information to extract is:

# The number of successful missions.
# The success rate of the missions.
# A list of all the missions that were launched before the year 2000.

mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

numberOfMissions = len(mission_names)  # The total number of space missions.

print(f"Total number of missions: {numberOfMissions}")

numberOfSuccessfulMissions = 0;
for i in mission_success :
    if i :
        numberOfSuccessfulMissions += 1

# Print the number of successful missions.
print(f"Number of successful missions: {numberOfSuccessfulMissions}")

# Print the success rate as a percentage.
successRate = numberOfSuccessfulMissions / numberOfMissions
print(f"Success rate: {successRate*100:,.2f}%")

mission = []
for i, year in enumerate(mission_years):
#    Identify and list all missions launched before the year 2000.
    if year < 2000 :
       mission.append(mission_names[i])

# Print the names of the missions launched before the year 2000.
print("Missions launched before the year 2000:")
for name in mission :
    print("- "+ name)
