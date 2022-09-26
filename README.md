## Menu-Pack
# Инсталяция
Pip:
```
pip3(pip) install 
```
Использование в коде:
```from Menu.core import MenuApp```
# Пример кода
```
from Menu.core import MenuApp
app = MenuApp(['kok', 'koko'], ['print hello', 'command://print(\'Hello!\''])
app.title('Test')
app.title_msgbox(')))')
app.init()
app.loop()
print('stoped     ;)')
```
