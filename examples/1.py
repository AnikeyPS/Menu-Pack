from menu.core import MenuApp
app = MenuApp(['README.md', '''print('d')
def a():
    print('aaa')
a()'''], ['Test setup', 'link://setup.test'])
app.title('Example window')
app.init()
app.loop()
