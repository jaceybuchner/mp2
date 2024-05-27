import random

# an implementation of random walk
# TODO: implement an algorithm better than random walk
def player1_logic(coins, potions, foods, dungeon_map, self_position, other_agent_position):
    # Directions are mapped to 'W', 'A', 'S', 'D'
    directions = {'W': (0, -1), 'A': (-1, 0), 'S': (0, 1), 'D': (1, 0)}
    
    # Get current position of the agent
    x, y = self_position
    
    # List to hold possible moves
    valid_moves = []
    
    # Check each possible direction
    for move in directions:
        dx, dy = directions[move]
        nx, ny = x + dx, y + dy
        
        # Ensure the new position is within the bounds of the map and is not a wall
        # Notice that you have to access position (x, y) via dungeon_map[y][x]
        # Because the dungeon_map is a list of lists
        if dungeon_map[ny][nx] == 'floor':
            valid_moves.append(move)
    
    # If there are no valid moves, return 'I' to remain idle
    if not valid_moves:
        return 'I'
    
    # Randomly choose from the valid moves
    return random.choice(valid_moves)

