from distutils.core import setup

setup(name='menu', version='0.2.0',
      packages=['menu', 'menu.files', 'menu_examples'],
      package_dir={'menu': 'menu', 'menu.files': 'menu\\files', 'menu_examples': 'examples'})
