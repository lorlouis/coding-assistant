# type: ignore
import sys

_old_hook = sys.excepthook

# I don't want to be sued my MS so I'll use a single 'p'
clipy = """
 _-_  | /
/_  \\ |/
(o)(o)
| | |
| \\/ /
\\    |
 ¯--¯"""


def assistant_print(type_, value, tb):
    _old_hook(type_, value, tb)
    width = len(f"{type_.__qualname__}{f': {value}' if value else ''}")-2
    print(f"\\{'_'*width}/" + clipy)



sys.excepthook = assistant_print
