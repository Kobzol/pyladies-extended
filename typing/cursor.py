import dataclasses
from typing import List, Optional, Tuple, Union

Position = Tuple[int, int]


class Button:
    def contains(self, position: Position) -> bool:
        return False


@dataclasses.dataclass
class Cursor:
    button_found: bool
    button_pressed: bool
    button: Button
    timer: float


class Screen:
    def __init__(self):
        self.cursor = Cursor()
        self.buttons: List[Button] = []

    def update(self, position: Position):
        found_button = None
        for button in self.buttons:
            if button.contains(position):
                found_button = button
                break
        if found_button is None:
            pass


CursorEnum = Union["FreeCursor", "CursorPressing", "CursorPressed"]


@dataclasses.dataclass
class FreeCursor:
    pass


@dataclasses.dataclass
class CursorPressing:
    button: Button
    timer: float = 0.0

    def finish_press(self) -> "CursorPressed":
        return CursorPressed(button=self.button)


@dataclasses.dataclass
class CursorPressed:
    button: Button



class ScreenEnum:
    def __init__(self):
        self.cursor: CursorEnum = FreeCursor()
        self.buttons: List[Button] = []
        self.selected_button: Optional[Button] = None

    def update(self, position: Position, delta: float):
        if isinstance(self.cursor, FreeCursor):
            for button in self.buttons:
                if button.contains(position):
                    self.cursor = CursorPressing(button=button)
                    break
        elif isinstance(self.cursor, CursorPressing):
            if self.cursor.button.contains(position):
                self.cursor.timer += delta
                if self.cursor.timer > 1.0:
                    self.cursor = self.cursor.finish_press()
                    self.selected_button = self.cursor.button
            else:
                self.cursor = FreeCursor()
        elif isinstance(self.cursor, CursorPressed):
            if not self.cursor.button.contains(position):
                self.cursor = FreeCursor()
        else:
            assert False
