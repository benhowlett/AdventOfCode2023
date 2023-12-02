def compare_cube_numbers(drawnCubes):
    return int(drawnCubes[0]) <= 12 and int(drawnCubes[1]) <= 14 and int(drawnCubes[2]) <= 13

def get_rgb_counts(draw):
    red = 0
    blue = 0
    green = 0
    for item in draw:
        match item[1]:
            case "red":
                red = item[0]
            case "blue":
                blue = item[0]
            case "green":
                green = item[0]
            case _:
                print("Error in draw colour")
    return red, blue, green

input = open("input", "r")

total = 0

for line in input:
    game = line.split(": ")
    gameNumber = int(game[0].split()[1])
    print(game[0])
    
    draws = game[1].strip().split("; ")
    print("Draws: ", draws)
    drawContents = []
    for draw in draws:
        drawnCubes = []
        for cubes in draw.split(", "):
            drawnCubes.append([cubes.split()[0], cubes.split()[1]]) 
        print("Drawn Cubes: ", drawnCubes)
        drawContents.append(get_rgb_counts(drawnCubes))
        print(drawContents)
    
    gameIsPossible = True

    for draw in drawContents:
        if not compare_cube_numbers(draw):
            gameIsPossible = False
    
    print(gameIsPossible)

    if gameIsPossible:
        # print(game[0], " is possible")
        total += gameNumber

print(total)

