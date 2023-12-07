def create_conversion_dict(input) -> {}:
    destinationRangeStart = int(input[0])
    sourceRangeStart = int(input[1])
    destinationRangeEnd = destinationRangeStart + int(input[2])
    sourceRangeEnd = sourceRangeStart + int(input[2])
    conversionDict = {}
    for index, sourceNumber in enumerate(range(sourceRangeStart, sourceRangeEnd)):
        conversionDict[sourceNumber] = range(destinationRangeStart, destinationRangeEnd)[index]
    return conversionDict

def merge_dicts(dict1, dict2) -> {}:
    mergedDict = {**dict1, **dict2}
    return mergedDict

input = open('test', 'r')
almanac = input.readlines()

seeds = []
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
            seeds = line.split(':')[1].strip().split()
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

seedToSoilMap = {}
soilToFertilizerMap = {}
fertilizerToWaterMap = {}
waterToLightMap = {}
lightToTempMap = {}
tempToHumMap = {}
humToLocMap = {}

for item in seedToSoilMapInput:
    tempDict = create_conversion_dict(item)
    seedToSoilMap = merge_dicts(seedToSoilMap, tempDict)
for item in soilToFertilizerMapInput:
    tempDict = create_conversion_dict(item)
    soilToFertilizerMap = merge_dicts(soilToFertilizerMap, tempDict)
for item in fertilizerToWaterMapInput:
    tempDict = create_conversion_dict(item)
    fertilizerToWaterMap = merge_dicts(fertilizerToWaterMap, tempDict)
for item in waterToLightMapInput:
    tempDict = create_conversion_dict(item)
    waterToLightMap = merge_dicts(waterToLightMap, tempDict)
for item in lightToTempMapInput:
    tempDict = create_conversion_dict(item)
    lightToTempMap = merge_dicts(lightToTempMap, tempDict)
for item in tempToHumMapInput:
    tempDict = create_conversion_dict(item)
    tempToHumMap = merge_dicts(tempToHumMap, tempDict)
for item in humToLocMapInput:
    tempDict = create_conversion_dict(item)
    humToLocMap = merge_dicts(humToLocMap, tempDict)

locations = []

for seed in seeds:
    # print(seed, type(seed))
    soil = int(seed)
    # print(seed, type(seed))
    for key in seedToSoilMap.keys():
        if key == int(seed):
            soil = seedToSoilMap[key]
    # print(soil, type(soil))
    fertilizer = soil
    for key in soilToFertilizerMap.keys():
        if key == soil:
            fertilizer = soilToFertilizerMap[key]
    # print(fertilizer, type(fertilizer))
    water = fertilizer
    for key in fertilizerToWaterMap.keys():
        if key == fertilizer:
            water = fertilizerToWaterMap[key]
    # print(water, type(water))
    light = water
    for key in waterToLightMap.keys():
        if key == water:
            light = waterToLightMap[key]
    # print(light, type(light))
    temp = light
    for key in lightToTempMap.keys():
        if key == light:
            temp = lightToTempMap[key]
    # print(temp, type(temp))
    hum = temp
    for key in tempToHumMap.keys():
        if key == temp:
            hum = tempToHumMap[key]
    # print(hum, type(hum))
    loc = hum
    for key in humToLocMap.keys():
        if key == hum:
            loc = humToLocMap[key]
    # print(loc, type(loc))
    locations.append(loc)

locations.sort()

print(locations[0])

