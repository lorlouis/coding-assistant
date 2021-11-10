# type: ignore
try:
    from .clipy import clipy
    from .assistant import set_excepthook
except (ImportError, ModuleNotFoundError):
    from clipy import clipy
    from assistant import set_excepthook

set_excepthook(clipy)
