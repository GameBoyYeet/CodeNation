# Part A: Sum of tuples

def sum_within_tuples(tuples: list) -> list:
  sums = []
  for x in tuples:
    sums.append(sum(x))
  return sums

# Part B: Friend calculator

def friend_calculator(friendships: list, n: int) -> list:
  people = []
  friend_counts = []

  # Create a list of people in the given friendships list
  
  for x in range(n):
    people.append(x)

  # Count how many times a person occurs in the given friendships list
  
  for x in people:
    friend_counts.append(0)
    for tup in friendships:
      if x in tup:
        friend_counts[-1] += 1

  return friend_counts

# Conway's Game of Life

# Part C1: Check if point is valid

def is_valid_indices(x: int, y: int, n: int) -> bool:
  return 0 <= x < n and 0 <= y < n

# Part C2: Check if square is populated

def is_populated(x: int, y: int, n: int, grid: list) -> bool:
  return is_valid_indices(x, y, n) and not grid[x][y] == ' '

# Part C3: Get neighbors of square

def get_neighbors(x: int, y: int) -> list:
  neighbors = []

  for i in range(-1, 2):
      if i == 0: # A cell is not a neighbor of itself!
        continue

      neighbors.append((x,y+i))
      neighbors.append((x+i,y))
      neighbors.append((x+i,y+i))
      neighbors.append((x+i,y-i))
  
  return neighbors

# Part C4: Number of populated neighbors

def num_populated_neighbors(x: int, y: int, n: int, grid: list) -> int:
  num_populated_neighbors = 0
  
  for j in get_neighbors(x,y):
    if is_populated(j[0], j[1], n, grid):
      num_populated_neighbors += 1
  
  return num_populated_neighbors

# Part C5: Determine if square lives

def will_live(x: int, y: int, n: int, grid: list) -> bool:
  populated_neighbors = num_populated_neighbors(x, y, n, grid)

  if is_populated(x, y, n, grid):
    if populated_neighbors in [2, 3]:
      return True
  else:
    if populated_neighbors == 3:
      return True
  
  return False

# Part C6: Update grid
def update_grid(n: int, grid: list) -> list:
  new_grid = [[' ' for i in range(n)] for j in range(n)]

  for x in range(n):
    for y in range(n):
      if will_live(x, y, n, grid):
        new_grid[x][y] = '+'
  
  return new_grid

# Part C7: Grid to string and print grid
def list_to_string(input: list) -> str:
  output = ''

  for i in range(len(input)):
    output += input[i]

  return output

def print_grid(n: int, grid: list) -> None:
  bchar = "#"

  print(bchar * (n+2))
  for i in range(n):
    print(bchar + list_to_string(grid[i]) + bchar)
  print(bchar * (n+2))

# Part C8: Run Conway's Game of Life

import os
import time

def clear_screen():
    # Check the operating system and use the appropriate command to clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    # Glider to easily test program
    grid = [
        [' ', ' ', ' ', ' ',' ', ' ', ' ', ' ',' ', ' '],
        [' ', ' ', ' ', ' ',' ', ' ', ' ', ' ',' ', ' '],
        [' ', ' ', ' ', ' ','+', ' ', ' ', ' ',' ', ' '],
        [' ', ' ', ' ', ' ',' ', '+', ' ', ' ',' ', ' '],
        [' ', ' ', ' ', '+','+', '+', ' ', ' ',' ', ' '],
        [' ', ' ', ' ', ' ',' ', ' ', ' ', ' ',' ', ' '],
        [' ', ' ', ' ', ' ',' ', ' ', ' ', ' ',' ', ' '],
        [' ', ' ', ' ', ' ',' ', ' ', ' ', ' ',' ', ' '],
        [' ', ' ', ' ', ' ',' ', ' ', ' ', ' ',' ', ' '],
        [' ', ' ', ' ', ' ',' ', ' ', ' ', ' ',' ', ' '],
    ]
    n=10

    # Extra: Stop program when grid stabilizes
    while True:
        last_grid = grid
        grid = update_grid(n,grid)
        print_grid(n,grid)
        if last_grid == grid:
          print("Grid has stabilized, stopping")
          break
        time.sleep(1/5)
        clear_screen()

main()