
def linear_distance(a, b):
    return abs(a.x - b.x) + abs(a.y - b.y)

def get_closest_point_to(source, targets):
    if len(targets) == 0: return None
    if len(targets) == 1: return targets[0]

    min_target = targets[0]
    min_distance = linear_distance(source, min_target)
    for target in targets[1:]:
        distance = linear_distance(source, target)
        if distance < min_distance:
            min_distance = distance
            min_target = target
    return min_target

def flood_fill(width, height, cells, sources):

    if len(cells) != width * height:
        raise Exception()

    counts = []
    queue = []
    groups = []
    for i, (x, y) in enumerate(sources):
        index = get_index(width, x, y)
        groups.append([i+1])
        queue.append(index)
        cells[index] = i+1
        counts.append(1)

    def flood(current_cell, next_x, next_y):
        if next_x < 0 or next_x >= width: return False
        if next_y < 0 or next_y >= height: return False
        next_cell = get_index(width, next_x, next_y)

        current_cell_value = cells[current_cell]
        next_cell_value = cells[next_cell]

        if next_cell_value == -1: return False
        elif next_cell_value == current_cell_value: return False
        elif next_cell_value == 0:
            cells[next_cell] = current_cell_value
            queue.append(next_cell)
            return True
        else:
            current_group = next(filter(lambda group: current_cell_value in group, groups))
            if cells[next_cell] in current_group: return False
            next_group = next(filter(lambda group: next_cell_value in group, groups))
            current_group.extend(next_group)
            groups.remove(next_group)
            return False

    while len(queue) > 0:
        current_cell = queue[0]
        queue = queue[1:]
        x, y = get_xy(width, current_cell)
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            if flood(current_cell, x + dx, y + dy):
                yield cells
    
def get_index(width, x, y):
    return width * y + x

def get_xy(width, index):
    x = index % width
    y = (index - x) // width
    return x, y 

if __name__ == "__main__":
    for x in [0,1,2]:
        for y in [0,1,2]:
            i = get_index(3, x, y)
            nx, ny = get_xy(3, i)
            print(f"{x},{y} {i} {nx},{ny}")

    obs = [(0, 1),(1, 1),(2, 1)]
    sources = [(0, 0), (2, 0)]
    print(flood_fill(3, 3, obs, sources))