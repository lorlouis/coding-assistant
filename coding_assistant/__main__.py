import sys
from pathlib import Path
from subprocess import Popen, PIPE

import coding_assistant


# Hardcoded values, helps refactoring for multiple assistants down the line
PATH_IDX = 1
ARGS_IDX = 2
ASSISTANT = coding_assistant.clipy


def cli():
    try:
        path = Path(sys.argv[PATH_IDX]).resolve()
    except IndexError:
        raise coding_assistant.AssistantException("Path to file is missing!") from None
    args = sys.argv[ARGS_IDX:]

    # Path to Python Interpreter
    python = sys.executable
    p = Popen([python, path, *args], text=True, stdin=sys.stdin, stdout=sys.stdout, stderr=PIPE)
    _, err = p.communicate()
    if err:
        # Normal encoding of the ASCII art was causing errors, this is Windows-1252, a legacy encoding scheme
        err = err

        # Break into lines
        split_assistant = ASSISTANT.splitlines()
        split_err = err.splitlines()

        # Prevent double assistant by comparing lines that should be equivalent
        # Skip first line due to funky spacing of decoded characters
        if split_assistant[1:] != split_err[-len(split_assistant)+1:]:
            width = len(split_err[-1]) - 2
            err += f"\\{'_' * width}/" + ASSISTANT

        print(err, file=sys.stderr)
    return p.returncode


if __name__ == '__main__':
    sys.exit(cli())
