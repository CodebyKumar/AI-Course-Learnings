from collections import deque
import time

def get_grid_from_user():
    """Get grid configuration from user"""
    rows = int(input("Enter grid size (n for n×n grid): "))
    grid = []

    print("\nEnter cell states (C=Clean, D=Dirty, O=Obstacle):")
    for i in range(rows):
        line = input(f"Row {i} (e.g., CD for 2 col): ").upper()
        row = [({'C': 'Clean', 'D': 'Dirty', 'O': 'Obstacle'}.get(char, 'Clean')) for char in line[:rows]]
        row.extend(['Clean'] * (rows - len(row)))  # Fill remaining columns with Clean cells
        grid.append(row)

    agent_pos = list(map(int, input("\nEnter agent position (row column): ").split()))
    charging_pos = tuple(map(int, input("\nEnter charging station position (row column): ").split()))

    return grid, agent_pos, charging_pos, rows

def display_grid(grid, agent_pos, charging_station, battery, rows):
    """Display grid with agent, charging station, etc."""
    symbols = {'Clean': '⬜', 'Dirty': '🍂', 'Obstacle': '⛔'}
    print("\nCurrent State:")
    for i in range(rows):
        for j in range(rows):
            if [i, j] == agent_pos:
                print("🤖", end=" ")
            elif (i, j) == charging_station:
                print("⚡", end=" ")
            else:
                print(symbols[grid[i][j]], end=" ")
        print()
    print(f"Battery: {battery}%\n")
    time.sleep(0.5)

def find_path(grid, start, is_goal, rows):
    """Find shortest path using BFS"""
    queue = deque([(start, [])])
    visited = {start}
    movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        (x, y), path = queue.popleft()
        if is_goal(x, y):
            return path
        for dx, dy in movements:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < rows and grid[nx][ny] != "Obstacle" and (nx, ny) not in visited:
                queue.append(((nx, ny), path + [(nx, ny)]))
                visited.add((nx, ny))
    return None

def run_agent(grid, agent_pos, charging_station, rows):
    """Execute goal-based agent's decision process"""
    battery = 100
    movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while True:
        display_grid(grid, agent_pos, charging_station, battery, rows)
        x, y = agent_pos
        
        if all(grid[i][j] != "Dirty" for i in range(rows) for j in range(rows)):
            print("All areas cleaned!")
            path = find_path(grid, (x, y), lambda i, j: (i, j) == charging_station, rows)
            if path:
                print("Returning to charging station...")
                for nx, ny in path:
                    agent_pos[0], agent_pos[1] = nx, ny
                    battery -= 2
                    time.sleep(0.3)
                print("Returned to charging station. Mission complete!")
            else:
                print("Cannot return to charging station, but all areas are clean.")
            break
        
        if grid[x][y] == "Dirty":
            print(f"Cleaning ({x}, {y})")
            grid[x][y] = "Clean"
            battery -= 5
            continue
        
        if any(0 <= x + dx < rows and 0 <= y + dy < rows and grid[x + dx][y + dy] == "Obstacle" for dx, dy in movements):
            print("Obstacles nearby, planning path...")
            if not any(0 <= x + dx < rows and 0 <= y + dy < rows and grid[x + dx][y + dy] != "Obstacle" for dx, dy in movements):
                print("Trapped by obstacles! Cannot move.")
                break
            for dx, dy in movements:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < rows and grid[nx][ny] != "Obstacle":
                    agent_pos[0], agent_pos[1] = nx, ny
                    battery -= 2
                    break
            continue
        
        if battery <= 15:
            print("Low battery! Returning to charging station...")
            path = find_path(grid, (x, y), lambda i, j: (i, j) == charging_station, rows)
            if path:
                for nx, ny in path:
                    agent_pos[0], agent_pos[1] = nx, ny
                    battery -= 2
                    time.sleep(0.3)
                print("Recharging...")
                battery = 100
                display_grid(grid, agent_pos, charging_station, battery, rows)
            else:
                print("Cannot reach charging station! Shutting down.")
                break
            continue
        
        nearest_path = min((find_path(grid, (x, y), lambda a, b: (a, b) == (i, j), rows) for i in range(rows) for j in range(rows) if grid[i][j] == "Dirty"), key=len, default=None)
        if nearest_path:
            next_x, next_y = nearest_path[0]
            agent_pos[0], agent_pos[1] = next_x, next_y
            battery -= 2
            print(f"Moving to ({next_x}, {next_y})")
        else:
            print("No accessible dirty squares!")
            break

def main():
    print("=== Goal-Based Agent: Vacuum Cleaner ===")
    grid, agent_pos, charging_station, rows = get_grid_from_user()
    run_agent(grid, agent_pos, charging_station, rows)

if __name__ == "__main__":
    main()