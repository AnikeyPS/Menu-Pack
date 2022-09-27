from menu.core import MenuApp
app = MenuApp(['Hello', 'Hello) ;-}'], ['Test setup', 'link://setup.test'])
app.title('Example window')
app.init()
app.loop()
