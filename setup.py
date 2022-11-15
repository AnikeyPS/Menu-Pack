from distutils.core import setup
from menu import __version__

setup(name='menu', version=__version__,
      packages=['menu', 'menu.files', 'menu_examples'],
      package_dir={'menu': 'menu_pack', 'menu_pack.files': 'menu\\files', 'menu_pack.examples': 'examples'})
