import threading as th
from menu_pack.core import MenuApp


def _run():
    app = MenuApp(["Button 1": "Read button", "Pause": "command://__import__('os').system('pause')"])
    app.init()
    app.loop()


obj = th.Thread(target=_run)
obj.start()
obj.join()
