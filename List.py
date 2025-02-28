justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print("Initial Justice League:", justice_league)

# 3.1 Count members
print("Number of members:", len(justice_league))

# 3.2 Add new members
justice_league.extend(["Batgirl", "Nightwing"])
print("After adding Batgirl and Nightwing:", justice_league)

# 3.3 Move Wonder Woman to the beginning
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("After making Wonder Woman the leader:", justice_league)

# 3.4 Move Superman between Aquaman and Flash
justice_league.remove("Superman")
justice_league.insert(justice_league.index("Flash"), "Superman")
print("After separating Aquaman and Flash:", justice_league)

# 3.5 Replace the team
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("New Justice League team:", justice_league)

# 3.6 Sort alphabetically
justice_league.sort()
print("Sorted Justice League:", justice_league)
print("New leader:", justice_league[0])
