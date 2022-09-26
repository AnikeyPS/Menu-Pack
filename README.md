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
# sys.argv
```-outOff``` - Отключает все принты кроме дебага.
```-debug``` - Включает дебаг.
# Запуск с sys.argv
```python(3) file-location -(debug or outOff)```
