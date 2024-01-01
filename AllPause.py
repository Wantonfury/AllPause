import psutil
import eel

# Global values (for debug atm)
KEY_PAUSE = 13

def loadSettings():
  with open("settings.txt", "r") as settings:
    lines = settings.readlines()
    
    for line in lines:
      line = line.replace("\n", "")
      columns = line.split(" ")
      print(columns)

def init():
  # Load saved settings
  loadSettings()
  
  # Initialize GUI
  eel.init("web")
  eel.start("index.html")

if __name__ == "__main__":
  init()