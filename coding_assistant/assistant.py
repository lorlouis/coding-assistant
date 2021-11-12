# type: ignore
import sys

_old_hook = sys.excepthook
_character = ""


def assistant_print(type_, value, tb):
    _old_hook(type_, value, tb)
    width = len(f"{type_.__qualname__}{f': {value}' if value else ''}")-2
    print(f"\\{'_'*width}/" + character)


def set_excepthook(assistant: str) -> None:
    global character
    character = assistant
    sys.excepthook = assistant_print
