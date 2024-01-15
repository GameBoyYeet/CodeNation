from os import name, system

player_turn = 1
move_char = {1: "X", 2: "O"}

def check_tie(grid: list) -> int:
    if not any(' ' in sublist for sublist in grid):
        return 1

    return 0

def check_player_win(grid: list) -> int:
    # Return 1 if Player 1 win
    # Return 2 if Player 2 win
    # Return 0 if none
    
    for x in grid: # Horizontal check
        if x[0] == x[1] == x[2]:
            if x[0] == 'X':
                return 1
            elif x[1] == 'O':
                return 2
    
    for x in range(3): # Vertical check
        if grid[0][x] == grid[1][x] == grid[2][x]:
            if grid[0][x] == 'X':
                return 1
            elif grid[0][x] == 'O':
                return 2
            
    if grid[0][0] == grid[1][1] == grid[2][2]: # Diagonal check 1
        if grid[0][0] == 'X':
            return 1
        if grid[0][0] == 'O':
            return 2
            
    if grid[0][2] == grid[1][1] == grid[2][0]:
        if grid[0][2] == 'X':
            return 1
        elif grid[0][2] == 'O':
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
    print(f"Player {player_turn}'s turn!")
    while True:
        try:
            move = input(f"Put an {move_char[player_turn]} on (Example: 1,3): ")
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
        elif check_tie(grid) == 1:
            print("Tie!")
            exit()
        grid = update_grid(user_prompt(grid), grid)

if __name__ == "__main__":
    main()