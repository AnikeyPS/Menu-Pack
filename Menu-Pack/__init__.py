__version__ = '0.2.0'

import sys

debug = False
if '-debug' in sys.argv:
    debug = True
out = True
if '-outOff' in sys.argv:
    out = False

if out:
    print("Version " + __version__)
if debug:
    print(sys.version)
    print('Debug on')
