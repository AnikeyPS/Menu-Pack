import threading as th
from menu_pack.core import MenuApp


def _run():
    app = MenuApp(["Button 1": "Real button", "Pause": "command://__import__('os').system('pause')"])
    app.init()
    app.loop()


obj = th.Thread(target=_run)
