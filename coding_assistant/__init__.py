# type: ignore
import sys

_old_hook = sys.excepthook

# I don't want to be sued by MS so I'll use a single 'p'
clipy = """
 _-_  | /
/_  \\ |/
(o)(o)
| | |
| \\/ /
\\    |
 ¯--¯"""


def pathname(obj):
    """Create qualified pathname for objs. eg. module.sub.obj, module.sub.inner.obj"""

    module = obj.__module__

    # TB doesn't include builtin path
    if module is None or module == "builtins":
        return obj.__name__
    return module + '.' + obj.__name__


def assistant_print(type_, value, tb):
    _old_hook(type_, value, tb)
    # Traceback is inconsistent about which path to use, `format_exception_only` displays relative paths,
    # dropping magic roots, eg. "__main__" but still formatting necessary message information
    # When the exception hook uses them, it drops absolute paths, eg. "__main__.Super.Sub" becomes "__main__.Sub"
    message = traceback.format_exception_only(value).pop().strip().split(": ", 1)
    message[0] = pathname(type_)
    width = len(": ".join(message)) - 2
    print(f"\\{'_' * width}/" + clipy, file=sys.stderr)


sys.excepthook = assistant_print
