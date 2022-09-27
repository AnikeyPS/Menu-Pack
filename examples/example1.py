from menu.core import MenuApp
app = MenuApp(['Click', 'command://print(\'Hello!\')'], ['About', 'This is a example code'])
app.title('Example')
app = MenuApp(['Hello', 'Hello) ;-}'], ['Test setup', 'link://setup.test'])
app.title('Example window')
app.init()
app.loop()
