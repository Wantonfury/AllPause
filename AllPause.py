import psutil
import eel
import json
import os
import keyboard
import screeninfo

# Default values
# ======================================================
PROCESS_CURRENT_ACTIVE = "WindowCurrent"

FILE_DATA = "data.json"
FILE_DATA_SETTINGS = "settings"
FILE_DATA_HOTKEYS = "hotkeys"

HOTKEY_DEFAULT = {
  "process": PROCESS_CURRENT_ACTIVE,
  "mod1": "",
  "mod2": "",
  "key": "PAUSE"
}
SETTINGS_DEFAULT = {
  "theme": "black",
  "width": "800",
  "height": "640",
  "start_minimized": False
}
# ======================================================

# Eel exposed functions
# ======================================================
@eel.expose
def createHotkey(process, mod1, mod2, key):
  new_hotkey = {
    "process": process,
    "mod1": mod1,
    "mod2": mod2,
    "key": key
  }
  
  data = loadData()
  data[FILE_DATA_HOTKEYS].append(new_hotkey)
  saveData(data)

@eel.expose
def checkModifier():
  if keyboard.is_modifier():
    return True
  return False

@eel.expose
def getKeyprocess():
  pass

@eel.expose
def getHotkeys():
  return loadData()[FILE_DATA_HOTKEYS]

@eel.expose
def removeHotkey(process, mod1, mod2, key):
  remove_hotkey = { process, mod1, mod2, key }
  
  data = loadData()
  for hotkey in data[FILE_DATA_HOTKEYS]:
    if (hotkey == remove_hotkey):
      data[FILE_DATA_HOTKEYS].remove(hotkey)
      break
  saveData(data)

@eel.expose
def addHotkey(process, mod1, mod2, key):
  add_hotkey = { process, mod1, mod2, key }
  
  data = loadData()
  for hotkey in data[FILE_DATA_HOTKEYS]:
    if hotkey == add_hotkey:
      return False # don't add hotkey, it already exists
  
  data[FILE_DATA_HOTKEYS].append(add_hotkey)
  saveData(data)
  return True

@eel.expose
def getProcesses():
  processList = list()
  
  for process in psutil.process_iter():
    processList.append(process.name())
  
  return processList

@eel.expose
def readKey(modifier, current):
  current = current.lower()
  
  while True:
    key = keyboard.read_key()
    print(keyboard.is_modifier(key) == modifier)
    
    if key == "ESC":
      return current
    elif keyboard.is_modifier(key) == modifier:
      return key.upper()
    
# ======================================================

def saveData(data):
  with open(FILE_DATA, "w") as settings:
    settings.write(json.dumps(data, indent=2))

def loadData():
  with open(FILE_DATA, "r") as settings:
    data = json.loads(settings.read())
  return data

def resetData():
  data = {}
  data[FILE_DATA_SETTINGS] = SETTINGS_DEFAULT
  data[FILE_DATA_HOTKEYS] = [HOTKEY_DEFAULT]
  saveData(data)

def getAvailableKeys():
  code = keyboard.read_key()
  print(code)
  pass

def init():
  # Create default data if none exists
  if not os.path.exists(FILE_DATA): resetData()
  
  # Load settings
  settings = loadData()[FILE_DATA_SETTINGS]
  
  # Initialize GUI
  monitor = {}
  
  for m in screeninfo.get_monitors():
    if m.is_primary:
      monitor = m
      break
  
  eel.init("web")
  eel.start("index.html", size=(settings["width"], settings["height"]), position=(monitor.width //2 - int(settings["width"]) // 2, monitor.height //2 - int(settings["height"]) // 2))

if __name__ == "__main__":
  init()