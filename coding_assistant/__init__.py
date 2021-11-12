# type: ignore
from coding_assistant.clipy import clipy
from coding_assistant.assistant import set_excepthook

set_excepthook(clipy)
