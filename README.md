# Coding Assistant 📎

Recreate the joys of Office Assistant from the comfort of the Python interpreter.

## How to use?

```python3
>>> import coding_assistant
>>> # nothing more is needed
>>> 3 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
\_______________________________/
 _-_  | /
/_  \ |/
(o)(o)
| | |
| \/ /
\    |
 ¯--¯
>>>
```

You can also invoke coding assistant as a python wrapper so that
even errors happening in the compile phase (ie bad imports and the likes)
will be handeled by coding assistant.

```bash
$ coding-assistant bad_import.py
Traceback (most recent call last):
  File "~/.local/bin/coding-assistant", line 8, in <module>
    sys.exit(cli())
  File "~/.local/lib/python3.9/site-packages/coding_assistant/cli.py", line 23, in cli
    exec(f.read(), {
  File "<string>", line 1, in <module>
ModuleNotFoundError: No module named 'nonexistant_module'
\_______________________________________________________/
 _-_  | /
/_  \ |/
(o)(o)
| | |
| \/ /
\    |
 ¯--¯
$
```

## How to install?

```bash
python3 -m pip install coding-assistant
```

## Q&A

> Is it possible to have other, maybe custom, assistants?

Not at the moment but if you can draw ascii art please submit a PR.

> Will this package break `try` `except` blocks?

No it only changes the way exceptions are printed not the actual exception.

> Is this code "production ready"?

Don't.

> Will you get sued by Microsoft?

Hopefully my ascii art is ugly enough that I can claim it's an original character.
