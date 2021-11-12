# type: ignore
import sys
try:
    from assistant import set_excepthook
    from clipy import clipy
except ModuleNotFoundError:
    from coding_assistant.assistant import set_excepthook
    from coding_assistant.clipy import clipy


def cli():
    if len(sys.argv) < 2:
        # in the future allow for --character=
        print(f"Usage: {sys.argv[0]} <program.py> [<args> [...]]")
        exit(1)
    # futureproofing
    character = clipy

    set_excepthook(character)
    with open(sys.argv[1], "r") as f:
        # remove argv[0] from sys.argv
        sys.argv.pop(0)
        exec(f.read(), {
            'sys.excepthook': sys.excepthook,
        })
