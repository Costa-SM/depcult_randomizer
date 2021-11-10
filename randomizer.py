


from os import read
import random
random.seed()

teams_file = open("times.txt", "r")
teams = []

for line in teams_file:
    teams.append(line.rstrip('\n'))

for team in range(len(teams)):
    random_number = random.randint(0, len(teams) - 1)
    print(teams[random_number])
    teams.pop(random_number)