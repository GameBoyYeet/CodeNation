from os import name, system

player_turn = 1

def check_player_win(grid: list) -> int:
    if ' ' not in grid:
        return -1
    
    for x in grid:
        # Horizontal check
        if x[0] == x[1] == x[2] and x[0] in ['X', 'O']:
            if x[0] == 'X':
                return 1
            elif x[1] == 'O':
                return 2
        for y in x:
            if y[0] == y[1] == y[2] and y[0] in ['X', 'O']:
                if y[0] == 'X':
                    return 1
                elif y[0] == 'O':
                    return 2
    return 0

def print_grid(grid: list) -> None:
    system('clear' if name == 'posix' else 'cls')
    bchar = '#'
    print(bchar*7)
    for x in range(3):
        for y in range(3):
            print(bchar, end="")
            print(grid[x][y], end="")
        print(bchar)
    print(bchar*7)

def user_prompt(grid: list) -> tuple:
    global player_turn
    print("Player 1's turn!") if player_turn == 1 else print("Player 2's turn!")
    while True:
        try:
            move = input("Put an X on (Example: 1,3): ") if player_turn == 1 else input("Put an O on (Example: 1,3): ")
            move = tuple(map(int, move.split(',')))
            if 1 <= move[0] <=3 and 1 <= move[1] <= 3:
                if grid[move[1]-1][move[0]-1] != ' ':
                    print("This spot is already taken.")
                    continue
                break
            else:
                continue
        except KeyboardInterrupt:
            print()
            exit()
        except:
            continue

    return move

def update_grid(move: tuple, grid: list) -> list:
    global player_turn
    newgrid = grid

    if player_turn == 1:
        newgrid[move[1]-1][move[0]-1] = 'X'
        player_turn = 2
    elif player_turn == 2:
        newgrid[move[1]-1][move[0]-1] = 'O'
        player_turn = 1
    
    return newgrid


def main():
    grid = [[' ' for i in range(3)] for j in range(3)]
    while True:
        print_grid(grid)
        if check_player_win(grid) == 1:
            print("Player 1 won!")
            exit()
        elif check_player_win(grid) == 2:
            print("Player 2 won!")
            exit()
        elif check_player_win(grid) == -1:
            print("Tie!")
            exit()
        else:
            print("Debug: No one won yet")
        grid = update_grid(user_prompt(grid), grid)

if __name__ == "__main__":
    main()