import threading

def thread_loop(obj):
    def _run(app):
        copy_app = app
        copy_app.loop()
    thread_obj = threading.Thread(traget=_run, args=(obj))
    thread_obj.start()
    thread_obj.join()