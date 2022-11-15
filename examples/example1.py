from menu_pack.core import MenuApp
app = MenuApp(['Click', 'command://print(\'Hello!\')'], ['About', 'This is a example code'])
app.title('Example window')
app.init()
