PLACE = 'PLACE'
MOVE = 'MOVE'
LEFT = 'LEFT'
RIGHT = 'RIGHT'
REPORT = 'REPORT'
NORTH = 'NORTH'
SOUTH = 'SOUTH'
EAST = 'EAST'
WEST = 'WEST'
DIRECTIONS = [NORTH, SOUTH, EAST, WEST]
game_start = False

gridarr = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]

square = {
    0: None,
    1: None,
    2: None,
    3: None,
    4: None
}

grid = {
    0: square,
    1: square,
    2: square,
    3: square,
    4: square
}


def in_directions_list(str):
    return set(DIRECTIONS).intersection([str])


def place_coordinates(str):
    try:
        commands = str.split(" ")
        if commands[0] != PLACE:
            return False
        posits = commands[1].split(",")
        if len(posits) != 3 or not in_directions_list(posits[2]):
            return False
        return [int(posits[0]), int(posits[1]), posits[2]]
    except:
        return False


def main():
    print('Enter toy robot commands')
    command = input()
    while command != 'REPORT':
        command = input()
    print(command)


if __name__ == '__main__':
    main()
