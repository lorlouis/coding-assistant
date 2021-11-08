import sys

old_hook = sys.excepthook

assistant = """\\_______________________________/
 _-_  | /
/_  \\ |/
(o)(o)
| | |
| \\/ /
\\    |
 ¯--¯"""


def assistant_print(type_, value, traceback):
    old_hook(type_, value, traceback)
    print(assistant)


sys.excepthook = assistant_print
