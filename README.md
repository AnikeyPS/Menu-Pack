## Menu-Pack

# Инсталяция

Pip:

```
pip(3) install https://github.com/AnikeyPS/Menu-Pack/archive/main.zip
```

Использование в коде:

```
import menu
```

# Пример кода

```
from menu.core import MenuApp
app = MenuApp(['Click', 'command://print(\'Hello!\')'], ['About', 'This is a example code'])
app.title('Example')
app.init()
app.loop()
```

# sys.argv

`-outOff` - Отключает все принты кроме дебага.

`-debug` - Включает дебаг.

Запуск с sys.argv:

```
python(3) file-location -(debug or outOff)
```
