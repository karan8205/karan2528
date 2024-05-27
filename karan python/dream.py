from itertools import combinations

def generate_teams(all_rounders, bowlers, batsmen, keepers):
    # Initialize an empty list to store valid teams
    valid_teams = []

    # Generate combinations of players
    for i in range(1, len(all_rounders) + 1):
        for j in range(1, len(bowlers) + 1):
            for k in range(1, len(batsmen) + 1):
                for l in range(1, len(keepers) + 1):
                    # Check if the combination satisfies the criteria
                    if i + j + k + l == 11:
                        team = [all_rounders[a] for a in combinations(range(len(all_rounders)), i)]
                        team.extend([bowlers[b] for b in combinations(range(len(bowlers)), j)])
                        team.extend([batsmen[c] for c in combinations(range(len(batsmen)), k)])
                        team.extend([keepers[d] for d in combinations(range(len(keepers)), l)])
                        valid_teams.append(team)
    
    return valid_teams

# Example usage:
all_rounders = ["AR1", "AR2", "AR3", "AR4", "AR5", "AR6", "AR7", "AR8"]
bowlers = ["Bowler1", "Bowler2", "Bowler3", "Bowler4", "Bowler5", "Bowler6", "Bowler7"]
batsmen = ["Batsman1", "Batsman2", "Batsman3", "Batsman4"]
keepers = ["Keeper1", "Keeper2", "Keeper3"]

teams = generate_teams(all_rounders, bowlers, batsmen, keepers)

# Print the generated teams
for idx, team in enumerate(teams):
    print(f"Team {idx + 1}: {team}")
f=open("dream11teams.txt","w")
for i in valid_teams:
    f.write(i)
f.close()
    
    
