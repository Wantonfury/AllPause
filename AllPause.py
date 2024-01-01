import psutil
import eel

def saveSettings(keys):
  with open("settings.txt", "w") as settings:
    for key in keys:
      settings.write(key[0] + " " + str(key[1]) + " " + str(key[2]) + " " + str(key[3]) + "\n")

def loadSettings(keys):
  with open("settings.txt", "r") as settings:
    lines = settings.readlines()
    
    if len(lines) <= 0:
      keys.append(["All", 17, 16, 19])
      return
    
    for line in lines:
      line = line.replace("\n", "")
      columns = line.split(" ")
      keys.append([columns[0], int(columns[1]), int(columns[2]), int(columns[3])])

def init():
  keys = []
  
  # Load saved settings
  loadSettings(keys)
  print(keys)
  saveSettings(keys)
  
  # Initialize GUI
  eel.init("web")
  eel.start("index.html")

if __name__ == "__main__":
  init()