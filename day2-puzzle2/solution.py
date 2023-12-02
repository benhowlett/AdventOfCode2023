def get_rgb_counts(draw):
    red = 0
    blue = 0
    green = 0
    for item in draw:
        match item[1]:
            case "red":
                red = int(item[0])
            case "blue":
                blue = int(item[0])
            case "green":
                green = int(item[0])
            case _:
                print("Error in draw colour")
    return red, blue, green

input = open("input", "r")

total = 0

for line in input:
    game = line.split(": ")
    gameNumber = int(game[0].split()[1])
    # print(game[0])
    
    draws = game[1].strip().split("; ")
    # print("Draws: ", draws)
    drawContents = []
    for draw in draws:
        drawnCubes = []
        for cubes in draw.split(", "):
            drawnCubes.append([cubes.split()[0], cubes.split()[1]]) 
        # print("Drawn Cubes: ", drawnCubes)
        drawContents.append(get_rgb_counts(drawnCubes))
        # print(drawContents)
    
    minimumCubes = [0, 0, 0]

    for draw in drawContents:
        if draw[0] > minimumCubes[0]:
            minimumCubes[0] = draw[0]
        if draw[1] > minimumCubes[1]:
            minimumCubes[1] = draw[1]
        if draw[2] > minimumCubes[2]:
            minimumCubes[2] = draw[2]

    total += minimumCubes[0] * minimumCubes[1] * minimumCubes[2]   

print(total)

