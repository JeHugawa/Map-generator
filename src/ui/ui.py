from tkinter import Tk, Button
from ui.main_view import MainView


class UI(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #see: https://stackoverflow.com/questions/17466561/best-way-to-structure-a-tkinter-application


        self._view = None
        self.title("Map Generator")
        self.show_main_view()


    def destroy_view(self):
        if self._view:
            self._view.destroy()
        self._view = None


    def show_main_view(self):
        self.destroy_view()
        
        self._view = MainView(self)
