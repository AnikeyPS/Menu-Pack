from menu.core import MenuApp
example = MenuApp(['Click', 'command://print(\'Hello!\')'], ['About', 'This is a example code'])
example.title('Example')
example = MenuApp(['Hello', 'Hello) ;-}'], ['Test setup', 'link://setup.test'])
example.title('Example window')
example.init()
example.loop()
