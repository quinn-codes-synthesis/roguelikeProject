import tcod

from actions import EscapeAction, MovementAction
from input_handlers import EventHandler

def main() -> None:
    # variables for screen size
    screen_width = 80
    screen_height = 50

    # tracks the player's position
    # int() casts the result (a float) into an int
    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    # tells tcod which font to use
    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    # event_handler is an instance of our EventHandler class
    event_handler = EventHandler()

    # creates the screen
    with tcod.context.new_terminal(
            screen_width,
            screen_height,
            tileset=tileset,
            title="Untitled Roguelike Project",
            vsync=True,
    ) as context:
        # creates our console.
        # order="F" changes numpy to access 2D arrays in [x, y] order.
        root_console = tcod.Console(screen_width, screen_height, order="F")
        # game loop
        while True:
            # tells the console to print our symbol at the given coords
            root_console.print(x=player_x, y=player_y, string="@")

            # updates the screen with what we've told it to display
            context.present(root_console)

            # clears previous draw
            root_console.clear()

            # waits for input from the user
            for event in tcod.event.wait():
                # sort the action using event_handler
                action = event_handler.dispatch(event)

                # skip over the rest of the loop if action is None
                if action is None:
                    continue

                # draws player movement
                if isinstance(action, MovementAction):
                    player_x += action.dx
                    player_y += action.dy

                # if escape key is pressed, exit program
                elif isinstance(action, EscapeAction):
                    raise SystemExit()


if __name__ == "__main__":
    main()