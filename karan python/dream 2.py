import itertools

# Players data
all_rounders = ["AR1", "AR2", "AR3", "AR4", "AR5", "AR6", "AR7", "AR8"]
bowlers = ["B1", "B2", "B3", "B4", "B5", "B6", "B7"]
batsmen = ["BAT1", "BAT2", "BAT3", "BAT4"]
keepers = ["K1", "K2", "K3"]

# Total players required for a team
total_players = 11

# Generate all combinations
team_combinations = itertools.combinations(all_rounders + bowlers + batsmen + keepers, total_players)

# Filter combinations to get valid teams
valid_teams = []
for team in team_combinations:
    # Count the number of players from each category
    all_rounder_count = sum(1 for player in team if player in all_rounders)
    bowler_count = sum(1 for player in team if player in bowlers)
    batsman_count = sum(1 for player in team if player in batsmen)
    keeper_count = sum(1 for player in team if player in keepers)
    # Check if each category is represented at least once
    if all_rounder_count >= 1 and bowler_count >= 1 and batsman_count >= 1 and keeper_count >= 1:
        valid_teams.append(team)

# Print valid teams
#for i, team in enumerate(valid_teams, start=1):
#    print(f"Team {i}: {team}")
print(len(valid_teams))
with open("cottect all teams.txt","w")as file:
    for i ,team in enumerate(valid_teams,start=1):
        file.write(f"Team {i}:{team}\n")


