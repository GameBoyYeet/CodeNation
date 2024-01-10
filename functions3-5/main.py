from os import name,system

player_turn = 1
emoji_mode = 0

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
    global emoji_mode
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
            if move == "emoji":
                emoji_mode = 1
                print("Emoji mode activated!")
            elif move == "text":
                print("Emoji mode deactivated!")
                emoji_mode = 0
            continue

    return move

def update_grid(move: tuple, grid: list) -> list:
    global emoji_mode
    global player_turn
    newgrid = grid

    player1char = '\U0000274C' if emoji_mode == 1 else 'X'
    player2char = '\U0001F1F4' if emoji_mode == 1 else 'O'

    if player_turn == 1:
        newgrid[move[1]-1][move[0]-1] = player1char
        player_turn = 2
    elif player_turn == 2:
        newgrid[move[1]-1][move[0]-1] = player2char
        player_turn = 1
    
    return newgrid


def main():
    grid = [[' ' for i in range(3)] for j in range(3)]
    while True:
        print_grid(grid)
        grid = update_grid(user_prompt(grid), grid)

if __name__ == "__main__":
    main()