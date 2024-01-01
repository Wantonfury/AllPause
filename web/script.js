const KEY_NONE = "NONE"
const CNT_HOTKEYS = document.querySelector("#list-hotkeys")
processes = []

readKey = (e, modifier) => {
  keyRead = (key) => {
    e.target.innerText = key
  }
  eel.readKey(modifier, e.target.innerText)(keyRead)
}

add_hotkey = (hotkey) => {
  elementCnt = document.createElement("div");
  elementProcess = document.createElement("input")
  elementMod1 = document.createElement("button")
  elementMod2 = document.createElement("button")
  elementKey = document.createElement("button")
  
  elementCnt.appendChild(elementProcess)
  elementCnt.appendChild(elementMod1)
  elementCnt.appendChild(elementMod2)
  elementCnt.appendChild(elementKey)
  
  elementCnt.classList.add("cnt-grid")
  
  elementProcess.type = "text"
  elementProcess.value = hotkey.process
  elementMod1.innerText = hotkey.mod1.length === 0 ? KEY_NONE : hotkey.mod1
  elementMod2.innerText = hotkey.mod2.length === 0 ? KEY_NONE : hotkey.mod2
  elementKey.innerText = hotkey.key
  
  elementMod1.addEventListener("click", (e) => readKey(e, true))
  elementMod2.addEventListener("click", (e) => readKey(e, true))
  elementKey.addEventListener("click", (e) => readKey(e, false))
  
  CNT_HOTKEYS.appendChild(elementCnt)
}

eel.expose
displayHotkeys = (hotkeys) => {
  //hotkeys = eel.getHotkeys()
  console.log(hotkeys)
}

initHotkeys = (hotkeys) => {
  console.log(hotkeys)
  for (hotkey of hotkeys) {
    add_hotkey(hotkey)
  }
}

initProcesses = (processList) => {
  processes = processList
}

eel.getHotkeys()(initHotkeys)
eel.getProcesses()(initProcesses)