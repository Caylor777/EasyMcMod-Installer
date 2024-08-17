import json, os, shutil
from ui import ui

f = open("settings.json")
settingsJSON = json.load(f)
f.close()

if settingsJSON["useJSON"]:
    pass

modsPath = ui.verifyModsPath(f"{os.getenv('APPDATA')}\\.minecraft\\mods\\")
if len(os.listdir(modsPath)) < 1:
    deletePreExistingMods = ui.managePreExistingMods(modsPath)

if deletePreExistingMods:
    for jar in os.listdir(modsPath):
        os.remove(f"{modsPath}\\{jar}")
else:
    os.makedirs("PreExistingMods")
    for jar in os.listdir(modsPath):
        os.replace(f"{modsPath}\\{jar}", f"PreExistingMods\\{jar}")
        
modsList = os.listdir("mods")

for jar in modsList:
    shutil.copy(f"mods\\{jar}", f"{modsPath}\\{jar}")