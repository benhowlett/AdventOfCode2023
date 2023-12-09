from tqdm import tqdm

def transform_number_from_mapping(number, maps) -> int:
    for map in maps:
        if number >= int(map[1]) and number < int(map[1]) + int(map[2]):
            number += int(map[0]) - int(map[1])
            break
    return number

def navigate_maps(seed, maps) -> int:
    for map in maps:
        seed = transform_number_from_mapping(seed, map)
    return seed

input = open('input', 'r')
almanac = input.readlines()

seedsInput = []
seedToSoilMapInput = []
soilToFertilizerMapInput = []
fertilizerToWaterMapInput = []
waterToLightMapInput = []
lightToTempMapInput = []
tempToHumMapInput = []
humToLocMapInput = []

for index, line in enumerate(almanac):
    if line != '\n':
        if line.split()[0] == 'seeds:':
            seedsInput = line.split(':')[1].strip().split()
        elif line.split()[0] == 'seed-to-soil':
            tempIndex = index
            while(tempIndex + 1 < len(almanac) and almanac[tempIndex + 1] != '\n'):
                tempIndex += 1
                seedToSoilMapInput.append(almanac[tempIndex].strip().split())
        elif line.split()[0] == 'soil-to-fertilizer':
            tempIndex = index
            while(tempIndex + 1 < len(almanac) and almanac[tempIndex + 1] != '\n'):
                tempIndex += 1
                soilToFertilizerMapInput.append(almanac[tempIndex].strip().split())
        elif line.split()[0] == 'fertilizer-to-water':
            tempIndex = index
            while(tempIndex + 1 < len(almanac) and almanac[tempIndex + 1] != '\n'):
                tempIndex += 1
                fertilizerToWaterMapInput.append(almanac[tempIndex].strip().split())
        elif line.split()[0] == 'water-to-light':
            tempIndex = index
            while(tempIndex + 1 < len(almanac) and almanac[tempIndex + 1] != '\n'):
                tempIndex += 1
                waterToLightMapInput.append(almanac[tempIndex].strip().split())
        elif line.split()[0] == 'light-to-temperature':
            tempIndex = index
            while(tempIndex + 1 < len(almanac) and almanac[tempIndex + 1] != '\n'):
                tempIndex += 1
                lightToTempMapInput.append(almanac[tempIndex].strip().split())
        elif line.split()[0] == 'temperature-to-humidity':
            tempIndex = index
            while(tempIndex + 1 < len(almanac) and almanac[tempIndex + 1] != '\n'):
                tempIndex += 1
                tempToHumMapInput.append(almanac[tempIndex].strip().split())
        elif line.split()[0] == 'humidity-to-location':
            tempIndex = index
            while(tempIndex + 1 < len(almanac) and almanac[tempIndex + 1] != '\n'):
                tempIndex += 1
                humToLocMapInput.append(almanac[tempIndex].strip().split())

maps = [
    seedToSoilMapInput,
    soilToFertilizerMapInput,
    fertilizerToWaterMapInput,
    waterToLightMapInput,
    lightToTempMapInput,
    tempToHumMapInput,
    humToLocMapInput
]

seeds = []

for index, value in enumerate(seedsInput):
    seeds.append([int(value), int(seedsInput[index + 1])])
    del seedsInput[index + 1]

lowestLocation = 999999999999999999

for index in tqdm(range(len(seeds))):
    for seed in tqdm(range(seeds[index][0], seeds[index][0] + seeds[index][1])):
        transformedSeedNumber = navigate_maps(seed, maps)
        if transformedSeedNumber < lowestLocation: lowestLocation = transformedSeedNumber

print(lowestLocation)

