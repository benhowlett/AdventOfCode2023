def count_winning_scenarios(race):
    count = 0
    for time in range(race[0]):
        if time * (race[0] - time) > race[1]:
            count += 1
    return count

input = open('input.txt', 'r')

times = []
distances = []

for line in input:
    if line.split()[0] == "Time:":
        times = line.split(':')[1].strip().split()
    else:
        distances = line.split(':')[1].strip().split()

races = []

for index, time in enumerate(times):
    races.append((int(time), int(distances[index])))

margin = 1

for race in races:
    margin *= count_winning_scenarios(race)

print(margin)