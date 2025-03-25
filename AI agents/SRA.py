import random
import time

# Initialize grid
size = 2
grid = [[random.choice(['Clean', 'Dirty']) for _ in range(size)] for _ in range(size)]
x, y = random.randint(0, size - 1), random.randint(0, size - 1)

def display_grid():
    for i in range(size):
        for j in range(size):
            if i == x and j == y: 
                print("🤖", end=" ")
            elif grid[i][j] == 'Dirty':
                print("🍂", end=" ")
            else:
                print("⬜", end=" ")
        print()
    print()

def sense_current_square():
    return grid[x][y]

def clean_current_square():
    global x, y
    print(f"Cleaning square at ({x}, {y})")
    grid[x][y] = 'Clean'
    time.sleep(1)

def move_to_next_square():
    global x, y
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    move = random.choice(moves)
    new_x = x + move[0]
    new_y = y + move[1]

    if 0 <= new_x < size and 0 <= new_y < size:
        x, y = new_x, new_y
        print(f"Moving to ({x}, {y})")
    else:
        print("Hit a wall. Trying again...")
    
    time.sleep(1)

def is_all_clean():
    return all(cell == 'Clean' for row in grid for cell in row)

# Run the agent
while not is_all_clean():
    display_grid()
    if sense_current_square() == 'Dirty':
        clean_current_square()
    else:
        move_to_next_square()


print("All squares are clean! Job done!")
