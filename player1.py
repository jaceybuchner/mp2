import heapq

def player1_logic(coins, potions, foods, dungeon_map, self_position, other_agent_position):
    # direction mappings
    directions = {'W': (0, -1), 'A': (-1, 0), 'S': (0, 1), 'D': (1, 0)}

    # (lower weight = higher priority)
    item_weights = {'coin': 1.0, 'potion': 0.8, 'food': 0.9}
    all_items = coins + potions + foods

    # uniform cost search
    frontier = []  # priority queue to store nodes to explore
    heapq.heappush(frontier, (0, self_position, []))  # initial position, cost=0, empty path
    explored = set()  # already explored posiitons

    while frontier:
        cost, current_pos, path = heapq.heappop(frontier)  # lowest cost node

        if current_pos in explored:
            continue  # skip if already explored 

        explored.add(current_pos)

        # if item at current spot
        if current_pos in all_items:
            return path[0] # returns one of the following: W, A, S, D

        # explore neighbors
        for move, (dx, dy) in directions.items():
            nx, ny = current_pos[0] + dx, current_pos[1] + dy
            if 0 <= nx < 40 and 0 <= ny < 30 and dungeon_map[ny][nx] == 'floor':
                new_cost = cost + 1  # move has cost of 1
                new_path = path + [move]
                heapq.heappush(frontier, (new_cost, (nx, ny), new_path))

    # No path to a coin found, remain idle
    return 'I'
