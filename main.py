MOVE = 'MOVE'
LEFT = 'LEFT'
RIGHT = 'RIGHT'
REPORT = 'REPORT'
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

def main():
    print('Enter toy robot commands')
    command = input()
    while command != 'REPORT':
        command = input()
    print(command)


if __name__ == '__main__':
    main()
