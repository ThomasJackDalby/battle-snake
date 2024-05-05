from fastapi import FastAPI 
from models import MoveRequest
from tools import get_closest_point_to

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
DIRECTIONS = ["up", "down", "left", "right"]

app = FastAPI()

@app.get("/")
def index():
    return {
        "apiversion": "1",
        "color": "#f56ce7",
        "head": "caffeine",
        "tail": "hook",
    }

@app.post("/start")
def start():
    pass

@app.post("/end")
def end():
    pass

@app.post("/move")
def move(request: MoveRequest):
    directions = Directions(request.you, request.board)
    directions.avoid_walls()
    directions.avoid_self()
    directions.avoid_snakes()
    directions.move_towards_closest_food()
    direction = next(directions.get_directions(), 0)
    return { "move": DIRECTIONS[direction] }

class Directions:

    def __init__(self, you, board):
        self.you = you
        self.board = board
        self.directions = [1,1,1,1]

    def avoid_walls(self):
        if self.you.head.x == 0: self.update(LEFT, 0)
        elif self.you.head.x == self.board.height - 1: self.update(RIGHT, 0)
        if self.you.head.y == 0: self.update(DOWN, 0)
        elif self.you.head.y == self.board.height - 1: self.update(UP, 0)

    def avoid_self(self):
        self.avoid_snake(self.you)

    def avoid_snakes(self):
        for snake in self.board.snakes:
            self.avoid_snake(snake)

    def avoid_snake(self, snake):
        head_x = self.you.head.x
        head_y = self.you.head.y

        for part in snake.body:
            if head_y == part.y:
                if head_x+1 == part.x: self.update(RIGHT, 0)
                elif head_x-1 == part.x: self.update(LEFT, 0)
            if head_x == part.x:
                if head_y+1 == part.y: self.update(UP, 0)
                elif head_y-1 == part.y: self.update(DOWN, 0)

    def move_towards_closest_food(self, factor=2):
        closest_food = get_closest_point_to(self.you.head, self.board.food)
        self.move_towards(closest_food, factor)

    def move_towards(self, point, factor):
        head_x = self.you.head.x
        head_y = self.you.head.y
        
        if point.y > head_y: self.update(UP, factor)
        elif point.y < head_y: self.update(DOWN, factor)
        if point.x < head_x:self.update(LEFT, factor)
        elif point.x > head_x: self.update(RIGHT, factor)

    def update(self, direction, factor):
        self.directions[direction] *= factor

    def get_directions(self):
        return (d for _, d in sorted(zip(self.directions, [0,1,2,3]), reverse=True))
    