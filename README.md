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
app = MenuApp(['Click', 'command://print(\'Hello!\')'], ['About', 'This is a example code'])
app.title('Example')
app.init()
app.loop()
```
# sys.argv
```-outOff``` - Отключает все принты кроме дебага.
```-debug``` - Включает дебаг.
# Запуск с sys.argv
```python(3) file-location -(debug or outOff)```
