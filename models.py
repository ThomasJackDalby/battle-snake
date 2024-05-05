from pydantic import BaseModel
from typing import Union, List

class Vector2D(BaseModel):
    x: int
    y: int

class Snake(BaseModel):
    id: str
    name: str
    health: int
    body: List[Vector2D]
    head: Vector2D
    length: int
    shout: Union[str, None]
    squad: Union[str, None]

class Board(BaseModel):
    width: int
    height: int
    food: List[Vector2D]
    snakes: List[Snake]

class MoveRequest(BaseModel):
    you: Snake
    board: Board