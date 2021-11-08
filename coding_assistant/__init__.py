# type: ignore
import sys

_old_hook = sys.excepthook

# I don't want to be sued my MS so I'll use a single 'p'
clipy = """\\_______________________________/
 _-_  | /
/_  \\ |/
(o)(o)
| | |
| \\/ /
\\    |
 ¯--¯"""


def assistant_print(type_, value, traceback):
    _old_hook(type_, value, traceback)
    print(clipy)


sys.excepthook = assistant_print
