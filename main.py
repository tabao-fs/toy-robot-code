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
    x = posits[0]
    y = posits[1]
    curr = posits[2]
    if turn == LEFT:
        if curr == NORTH:
            grid[x][y] = WEST
        elif curr == WEST:
            grid[x][y] = SOUTH
        elif curr == SOUTH:
            grid[x][y] = EAST
        elif curr == EAST:
            grid[x][y] = NORTH
    elif turn == RIGHT:
        if curr == NORTH:
            grid[x][y] = EAST
        elif curr == EAST:
            grid[x][y] = SOUTH
        elif curr == SOUTH:
            grid[x][y] = WEST
        elif curr == WEST:
            grid[x][y] = NORTH


def move_position(posits):
    x = posits[0]
    y = posits[1]
    dir = posits[2]

    if dir == NORTH and y + 1 <= 4:
        grid[x][y] = None
        grid[x][y + 1] = dir
    elif dir == EAST and x + 1 <= 4:
        grid[x][y] = None
        grid[x][x + 1] = dir
    elif dir == SOUTH and y - 1 >= 0:
        grid[x][y] = None
        grid[x][y - 1] = dir
    elif dir == WEST and x - 1 >= 0:
        grid[x][y] = None
        grid[x][x - 1] = dir


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
