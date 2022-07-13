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

        x = int(posits[0])
        y = int(posits[1])
        if (x < 0 or x > 4) or (y < 0 or y > 4):
            return False

        return [x, y, posits[2]]
    except:
        return False


def rotate_direction(posits, turn):
    curr = posits[2]
    if turn == LEFT:
        if curr == NORTH:
            grid[posits[0]][posits[1]] = WEST
        elif curr == WEST:
            grid[posits[0]][posits[1]] = SOUTH
        elif curr == SOUTH:
            grid[posits[0]][posits[1]] = EAST
        elif curr == EAST:
            grid[posits[0]][posits[1]] = NORTH
    elif turn == RIGHT:
        if curr == NORTH:
            grid[posits[0]][posits[1]] = EAST
        elif curr == EAST:
            grid[posits[0]][posits[1]] = SOUTH
        elif curr == SOUTH:
            grid[posits[0]][posits[1]] = WEST
        elif curr == WEST:
            grid[posits[0]][posits[1]] = NORTH


def move_position(posits):
    x = posits[0]
    y = posits[1]
    dir = posits[2]
    pass


def main():
    game_start = False
    print('Enter toy robot commands')
    while True:
        command = 'PLACE 0,0,NORTH'
        # command = input()
        posits = place_coordinates(command)

        if not game_start and posits is False:
            continue
        if not game_start:
            game_start = True

        if posits:
            grid[posits[0]][posits[1]] = posits[2]
        elif command == MOVE:
            move_position(posits)
        elif command == LEFT:
            rotate_direction(posits, LEFT)
        elif command == RIGHT:
            rotate_direction(posits, RIGHT)
        elif command == REPORT:
            pass
        break

    print(posits)


if __name__ == '__main__':
    main()
