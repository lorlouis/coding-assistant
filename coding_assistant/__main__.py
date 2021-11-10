# type: ignore
import sys

import default  # noqa


if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} <program.py> [<args> [...]]")
    exit(1)

with open(sys.argv[1], "r") as f:
    # remove argv[0] from sys.argv
    sys.argv.pop(0)
    exec(f.read(), {
        'sys.excepthook': sys.excepthook,
    })
