from re import X


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

grid = {
    0: { 0: None, 1: None, 2: None, 3: None, 4: None },
    1: { 0: None, 1: None, 2: None, 3: None, 4: None },
    2: { 0: None, 1: None, 2: None, 3: None, 4: None },
    3: { 0: None, 1: None, 2: None, 3: None, 4: None },
    4: { 0: None, 1: None, 2: None, 3: None, 4: None }
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


class Robot:
    def __init__(self, x, y, facing):
        self.x = x
        self.y = y
        self.facing = facing


    def rotate_direction(self, turn):
        if turn == LEFT:
            if self.facing == NORTH:
                grid[self.x][self.y] = WEST
            elif self.facing == WEST:
                grid[self.x][self.y] = SOUTH
            elif self.facing == SOUTH:
                grid[self.x][self.y] = EAST
            elif self.facing == EAST:
                grid[self.x][self.y] = NORTH
        elif turn == RIGHT:
            if self.facing == NORTH:
                grid[self.x][self.y] = EAST
            elif self.facing == EAST:
                grid[self.x][self.y] = SOUTH
            elif self.facing == SOUTH:
                grid[self.x][self.y] = WEST
            elif self.facing == WEST:
                grid[self.x][self.y] = NORTH


    def move_position(self):
        if self.facing == NORTH and self.y + 1 <= 4:
            grid[self.x][self.y] = None
            self.y += 1
            grid[self.x][self.y] = self.facing
        elif self.facing == EAST and self.x + 1 <= 4:
            grid[self.x][self.y] = None
            self.x += 1
            grid[self.x][self.y] = self.facing
        elif self.facing == SOUTH and self.y - 1 >= 0:
            grid[self.x][self.y] = None
            self.y -= 1
            grid[self.x][self.y] = self.facing
        elif self.facing == WEST and self.x - 1 >= 0:
            grid[self.x][self.y] = None
            self.x -= 1
            grid[self.x][self.y] = self.facing

        return [self.x, self.y, self.facing]


    def get_position(self):
        return f'{self.x},{self.y},{self.facing}'


def rotate_direction(posits, turn):
    x = posits[0]
    y = posits[1]
    facing = posits[2]
    if turn == LEFT:
        if facing == NORTH:
            grid[x][y] = WEST
        elif facing == WEST:
            grid[x][y] = SOUTH
        elif facing == SOUTH:
            grid[x][y] = EAST
        elif facing == EAST:
            grid[x][y] = NORTH
    elif turn == RIGHT:
        if facing == NORTH:
            grid[x][y] = EAST
        elif facing == EAST:
            grid[x][y] = SOUTH
        elif facing == SOUTH:
            grid[x][y] = WEST
        elif facing == WEST:
            grid[x][y] = NORTH


def move_position(posits):
    x = posits[0]
    y = posits[1]
    facing = posits[2]

    if facing == NORTH and y + 1 <= 4:
        grid[x][y] = None
        y += 1
        grid[x][y] = facing
    elif facing == EAST and x + 1 <= 4:
        grid[x][y] = None
        x += 1
        grid[x][y] = facing
    elif facing == SOUTH and y - 1 >= 0:
        grid[x][y] = None
        y -= 1
        grid[x][y] = facing
    elif facing == WEST and x - 1 >= 0:
        grid[x][y] = None
        x -= 1
        grid[x][y] = facing

    return [x, y, facing]


def get_position(posits):
    return f'{posits[0]},{posits[1]},{posits[2]}'


def run_robot():
    game_start = False
    cur_posit = None
    print('Enter toy robot commands')
    while True:
        command = input()
        posits = place_coordinates(command)

        if not game_start and posits is False:
            continue
        if not game_start:
            game_start = True

        if posits:
            if cur_posit:
                grid[cur_posit[0]][cur_posit[1]] = None
            grid[posits[0]][posits[1]] = posits[2]
            cur_posit = [posits[0], posits[1]]
        elif command == MOVE:
            posit = [cur_posit[0], cur_posit[1], grid[cur_posit[0]][cur_posit[1]]]
            cur_posit = move_position(posit)
        elif command == LEFT:
            posit = [cur_posit[0], cur_posit[1], grid[cur_posit[0]][cur_posit[1]]]
            rotate_direction(posit, LEFT)
        elif command == RIGHT:
            posit = [cur_posit[0], cur_posit[1], grid[cur_posit[0]][cur_posit[1]]]
            rotate_direction(posit, RIGHT)
        elif command == REPORT:
            posit = [cur_posit[0], cur_posit[1], grid[cur_posit[0]][cur_posit[1]]]
            return get_position(posit)


if __name__ == '__main__':
    res = run_robot()
    print(res)
