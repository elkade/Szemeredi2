from Program import Program
from GuiHandler import GuiHandler
from Window import Window
from threading import Lock

lock = Lock()
window = Window(lock)
handler = GuiHandler(window)
window.start()
Program.start(handler)
window.join()