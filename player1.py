import heapq

def player1_logic(coins, potions, foods, dungeon_map, self_position, other_agent_position):
    # direction mappings
    directions = {'W': (0, -1), 'A': (-1, 0), 'S': (0, 1), 'D': (1, 0)}

    # item priority
    item_priority = {item: 1 for item in potions + foods}  # high priority for potions and foods
    item_priority.update({item: 2 for item in coins})  # lower priority for coins

    frontier = []  # store nodes to explore, this is our heap
    heapq.heappush(frontier, (0, self_position, []))  # initial position, cost=0, empty path
    explored = set()  # already explored positions

    while frontier:
        # get the lowest cost node to explore
        cost, current_pos, path = heapq.heappop(frontier)

        # if explored then can skip it
        if current_pos in explored:
            continue  

        # mark as explored
        explored.add(current_pos)

        # if there is an item at current spot
        if current_pos in item_priority:
            return path[0] if path else 'I'  # return first move or 'I' if path is empty (fixed prev. bug)

        # explore neighbors
        for move, (dx, dy) in directions.items():
            x, y = current_pos
            nx, ny = x + dx, y + dy
            if 0 <= nx < 40 and 0 <= ny < 30 and dungeon_map[ny][nx] == 'floor':
                new_cost = cost + 1  # move has cost of 1
                if (nx, ny) in item_priority:
                    new_cost += item_priority[(nx, ny)] # add item priority to cost
                new_path = path + [move]
                heapq.heappush(frontier, (new_cost, (nx, ny), new_path))

    # no path to an item found, remain idle
    return 'I'
