class Action:
    pass


# subclass of Action. For using the Escape key.
class EscapeAction(Action):
    pass


# subclass of Action. For using movement keys.
class MovementAction(Action):
    def __init__(self, dx: int, dy: int):
        super().__init__()

        self.dx = dx
        self.dy = dy