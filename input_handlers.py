# for type hinting
from typing import Optional

# imports tcod's event system only
import tcod.event

from actions import Action, BumpAction, EscapeAction


# subclass of tcod's EventDispatch class
# sends an event to its proper method based on type of event
class EventHandler(tcod.event.EventDispatch[Action]):
    # receives quit events and quits the program
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    # receives keypress events and returns either Action subclass
    # or None, if no valid key was pressed
    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        # 'action' holds whatever subclass we end up assigning it to
        action: Optional[Action] = None

        # 'key' holds the key pressed.
        # Doesn't include modifiers i.e. shift, alt, ctrl
        key = event.sym

        # directional keys modify dx and dy
        if key == tcod.event.K_UP:
            action = BumpAction(dx=0, dy=-1)
        elif key == tcod.event.K_DOWN:
            action = BumpAction(dx=0, dy=1)
        elif key == tcod.event.K_LEFT:
            action = BumpAction(dx=-1, dy=0)
        elif key == tcod.event.K_RIGHT:
            action = BumpAction(dx=1, dy=0)

        elif key == tcod.event.K_ESCAPE:
            action = EscapeAction()

        return action
