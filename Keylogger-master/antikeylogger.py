import os
import time

var = os.system("TASKKILL /F /IM keylogger.exe")

import ctypes  # An included library with Python install.   
ctypes.windll.user32.MessageBoxW(0, "Keylogger has been terminated", "Keylogger", 1)