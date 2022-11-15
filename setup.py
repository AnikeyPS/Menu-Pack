from distutils.core import setup
from menu import __version__

setup(name='menu_pack', version=__version__,
      packages=['menu_pack', 'menu_pack.files', 'menu_pack.examples'],
      package_dir={'menu_pack': 'menu', 'menu_pack.files': 'menu\\files', 'menu_pack.examples': 'examples'})
