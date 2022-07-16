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
        new_facing = None
        if turn == LEFT:
            if self.facing == NORTH:
                new_facing = WEST
            elif self.facing == WEST:
                new_facing = SOUTH
            elif self.facing == SOUTH:
                new_facing = EAST
            elif self.facing == EAST:
                new_facing = NORTH
        elif turn == RIGHT:
            if self.facing == NORTH:
                new_facing = EAST
            elif self.facing == EAST:
                new_facing = SOUTH
            elif self.facing == SOUTH:
                new_facing = WEST
            elif self.facing == WEST:
                new_facing = NORTH

        self.facing = new_facing
        grid[self.x][self.y] = new_facing


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

        return self.list_current_position()


    def list_current_position(self):
        return [self.x, self.y, self.facing]


    def set_position(self, posits):
        self.x = posits[0]
        self.y = posits[1]
        self.facing = posits[2]


    def get_position(self):
        return f'{self.x},{self.y},{self.facing}'


def run_robot():
    game_start = False
    robot = None
    print('Enter toy robot commands')
    while True:
        command = input()
        posits = place_coordinates(command)

        if not game_start and posits is False:
            continue
        if not game_start:
            game_start = True

        if posits:
            if not robot:
                robot = Robot(posits[0], posits[1], posits[2])
            else:
                grid[robot.x][robot.y] = None
                robot.set_position([posits[0], posits[1], posits[2]])
            grid[robot.x][robot.y] = robot.facing
        elif command == MOVE:
            robot.move_position()
        elif command == LEFT:
            robot.rotate_direction(LEFT)
        elif command == RIGHT:
            robot.rotate_direction(RIGHT)
        elif command == REPORT:
            return robot.get_position()


if __name__ == '__main__':
    res = run_robot()
    print(res)
