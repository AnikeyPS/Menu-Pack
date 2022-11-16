import os
import sys
from .. import __version__
'''
This file is a list of new values.
Write new values down.
'''
setup = {
    '1': "Lol, kek, lol, kek, lol, kek",
    '2': "Hello ;>",
    '3': ";>",
    'versions': "POOP4ick",
    'dodoPIzza': 'ща if',
    'command': "command://print(\"I'm Jordi\")"
}

# Real setup commands
self_lib = {'__version__': __version__}
setup = {"setup": setup, "self": self_lib, "sys": sys.__dict__, "os": os.__dict__}
