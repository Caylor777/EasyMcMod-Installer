import json, os, shutil
from ui import ui

def main(installer: str, modsPath: str, deletePreExistingMods: bool):
    os.system(installer)
    if deletePreExistingMods:
        for jar in os.listdir(modsPath):
            os.remove(f"{modsPath}\\{jar}")
    else:
        os.makedirs("PreExistingMods")
        for jar in os.listdir(modsPath):
            os.replace(f"{modsPath}\\{jar}", f"PreExistingMods\\{jar}")
            
    modsList = os.listdir("mods")
    modsList.remove("ignore")
    
    for jar in modsList:
        shutil.copy(f"mods\\{jar}", f"{modsPath}\\{jar}")
        
def difineSettings():
    modsPath = ui.verifyModsPath(f"{os.getenv('APPDATA')}\\.minecraft\\mods\\")
    installer = ui.selectInstaller()
    if not os.path.exists(modsPath):
        os.makedirs(modsPath)

    if len(os.listdir(modsPath)) > 0:
        deletePreExistingMods = ui.managePreExistingMods(modsPath)
    else:
        deletePreExistingMods = True
    main(installer, modsPath, deletePreExistingMods)

#start
f = open("settings.json")
settingsJSON = json.load(f)
f.close()

if bool(settingsJSON["useJSON"]):
    try:
        settingsJSON["modsPath"].replace(f"%appdata%", os.getenv('APPDATA'))
    except:
        pass
    deletePreExistingMods = settingsJSON["deletePreExistingMods"]
    main(settingsJSON["installer"], settingsJSON["modsPath"], deletePreExistingMods)
else:
    difineSettings()