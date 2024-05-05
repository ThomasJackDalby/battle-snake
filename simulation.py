DXY = [(1,0),(-1,0),(0,1),(0,-1)]

class Snake:
    def __init__(self, id, body):
        self.id = id
        self.body = body
        self.head = body[0]

    def move(self, direction):
        dx, dy = DXY[direction]
        head = (self.head[0]+dx, self.head[1]+dy)
        body = [head] + self.body[1:]
        return Snake(self.id, body)

    def __repr__(self):
        return f"{self.id}:{self.head}"

class Simulation:

    def __init__(self, snakes):
        self.snakes = snakes

    def move(self, snake_id, snake_direction):
        snakes = [snake for snake in self.snakes]
        snakes[snake_id] = snakes[snake_id].move(snake_direction)
        return Simulation(snakes)

    def __repr__(self):
        return "["+"][".join(str(snake) for snake in self.snakes) + "]"
 
simulation = Simulation([Snake(0, [(0, 0), (1, 0)])])
current_simulations = [simulation]
for turn in range(2):
    next_simulations = []
    for simulation in current_simulations:
        for snake_id in range(len(simulation.snakes)):
            for direction in range(4):
                next_simulations.append(simulation.move(snake_id, direction))
    current_simulations = next_simulations
    print(current_simulations)

                