from menu_pack.core import MenuApp
example = MenuApp(['Click', 'command://print(\'Hello!\')'], ['About', 'This is a example code'])
example.title('Example window')
example.init()
example.loop()
