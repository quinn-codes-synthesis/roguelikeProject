from typing import Tuple


class Entity:
    """
    A generic object to represent players, enemies, items, etc.
    """
    def __init__(self, x: int, y: int, char: str, color: Tuple[int, int, int]):
        self.x = x
        self.y = y
        # the char used to represent the entity
        self.char = char
        # a tuple of ints, representing RGB values
        self.color = color

    def move(self, dx: int, dy: int) -> None:
        # Move the entity by a given amount
        self.x += dx
        self.y += dy
