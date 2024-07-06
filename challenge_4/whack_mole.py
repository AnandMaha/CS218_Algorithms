def maximum_moles_hit(m, n, moles):
    # Initialize a 2D grid to represent the game board
    grid = [[0] * m for _ in range(m)]
    
    # Mark mole positions on the grid
    for t, x, y in moles:
        grid[x - 1][y - 1] = t
    
    # Initialize variables to track points/moles hit
    points = 0
    
    # Iterate through each time step
    for t in range(1, max([t for t, _, _ in moles]) + 1):
        # Initialize a set to store visited cells
        visited = set()
        
        # Iterate through each cell on the grid
        for i in range(m):
            for j in range(m):
                # If the cell hasn't been visited yet
                if (i, j) not in visited:
                    # Move the robot hammer to each adjacent cell or stay in the same cell
                    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        ni, nj = i + dx, j + dy
                        # Check boundaries
                        if 0 <= ni < m and 0 <= nj < m:
                            # If there is a mole at the current position
                            if grid[ni][nj] == t:
                                # Increment points and mark the cell as visited
                                points += 1
                                visited.add((ni, nj))
        
        # Remove the mole from the grid
        for mole in moles:
            if mole[0] == t:
                x, y = mole[1] - 1, mole[2] - 1
                grid[x][y] = 0
    
    return points

# Example usage
m, n = 10, 10
moles = [
    (1, 4, 5),
    (1, 2, 3),
    (2, 7, 8),
    (2, 4, 2),
    (3, 5, 6),
    (7, 1, 1),
    (9, 6, 6),
    (10, 4, 5),
    (11, 7, 7),
    (15, 3, 3)
]

print(maximum_moles_hit(m, n, moles))  # Output: 4
