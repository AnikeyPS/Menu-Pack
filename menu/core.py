from .app import elements_print, element_get_value
import tkinter as tk
import tkinter.messagebox as msgbox_tk
from . import out, debug
from idlelib import __path__ as icon_path
from _tkinter import TclError
import ttk


def msgbox(name, title='Value'):
    name = element_get_value(name)
    msgbox_tk.showinfo(title, name)


class MenuApp:
    def __init__(self, *args):
        if args:
            self._elements = list(args)
            self._non_args = False
        else:
            self._elements = [['about', 'link://___.__help__'], ['python version', 'link://sys.version'],
                              ['test', 'test']]
            self._non_args = True
        self._main = tk.Tk()
        self._msgbox_title = 'Value'
        self._buttons = []

    def get_elements(self):
        return self._elements, elements_print(self._elements)

    def init(self):
        if self._buttons:
            for i in self._buttons:
                i.destroy()
        for i in self._elements:
            if i[1].startswith('command://'):
                self._buttons.append(self._add_command_button(i))
            else:
                if element_get_value(i).startswith('command://'):
                    list_ = i
                    list_[1] = element_get_value(list_)
                    self._buttons.append(self._add_command_button(list_))
                else:
                    self._buttons.append(self._add_button(i))
        icon = '{}\\Icons\\idle.ico'
        icon = icon.format(icon_path[0])
        self._main.wm_iconbitmap(icon)
        self._main.title("Menu demo")
        if out:
            print('Inited')

    def title(self, item):
        self._main.title(item)

    def update(self):
        self._main.update()

    def loop(self):
        if out:
            print('Started')
        while True:
            try:
                self._main.update()
            except TclError:
                if out:
                    print('Closed')
                break

    def add_item(self, item):
        if self._non_args:
            self._elements = []
        self._elements.append(item)

    def title_msgbox(self, item):
        self._msgbox_title = item

    def _add_button(self, list_):
        but = ttk.Button(self._main, text=list_[0],
                         command=lambda: msgbox(list_, self._msgbox_title))
        but.pack()
        return but

    def _add_command_button(self, list_):
        text = ''.join(list_[1].split('command://')[1:])
        if debug:
            print(text)
        but = ttk.Button(self._main, text=list_[0],
                         command=lambda: exec(text))
        but.pack()
        return but

    def icon(self, icon):
        self._main.wm_iconbitmap(icon)
        
