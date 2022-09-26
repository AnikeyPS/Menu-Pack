from . import out
__help__ = '''You can use this libraries:
sys,
this library (self),
print function,
file "setup.py",
os and
commands'''
__version__ = '1.2.0'


def main():
    print(__help__, end='\n\n')
    if out:
        print("Help version " + str(__version__))
