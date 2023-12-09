def count_winning_scenarios(race):
    count = 0
    for time in range(race[0]):
        if time * (race[0] - time) > race[1]:
            count += 1
    return count

def number_from_list(list):
    print(list)
    number = ""
    for item in list:
        number += item
    print(number)
    return int(number)

input = open('input.txt', 'r')

times = []
distances = []

for line in input:
    if line.split()[0] == "Time:":
        times = [number_from_list(line.split(':')[1].strip().split())]
    else:
        distances = [number_from_list(line.split(':')[1].strip().split())]

races = []

for index, time in enumerate(times):
    races.append((int(time), int(distances[index])))

print(races)

margin = 1

for race in races:
    margin *= count_winning_scenarios(race)

print(margin)