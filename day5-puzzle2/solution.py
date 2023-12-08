def transform_number_from_mapping(number, maps) -> int:
    for map in maps:
        if number >= int(map[1]) and number < int(map[1]) + int(map[2]):
            number += int(map[0]) - int(map[1])
            break
    return number

input = open('test', 'r')
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

seeds = []

for value in seedsInput:
    seeds.append(int(value))

lowestLocation = 999999999999999999

for index in range(int(len(seeds)/2)):
    for seed in range(seeds[index*2], seeds[index*2] + seeds[(index*2)+1]):
        soil = transform_number_from_mapping(seed, seedToSoilMapInput)
        fertilizer = transform_number_from_mapping(soil, soilToFertilizerMapInput)
        water = transform_number_from_mapping(fertilizer, fertilizerToWaterMapInput)
        light = transform_number_from_mapping(water, waterToLightMapInput)
        temp = transform_number_from_mapping(light, lightToTempMapInput)
        hum = transform_number_from_mapping(temp, tempToHumMapInput)
        loc = transform_number_from_mapping(hum, humToLocMapInput)
        if loc < lowestLocation:
            lowestLocation = loc

print(lowestLocation)

