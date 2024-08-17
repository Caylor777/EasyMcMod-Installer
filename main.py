import sys, json, os, shutil
from ui import ui

downloads = {}
loader = ""

#collect args
args = sys.argv
if len(args) < 2:
    raise IndexError("1 argument must be passed")
if args[1] == "fabric" or args[1] == "forge":
    loader = args[1]
else:
    raise TypeError(f"\"{args[1]}\" is not a valid argument, must be \"forge\" or \"fabric\"")

#read fiiles to download
downloadsDir = "downloads.json"
if len(args) > 2:
    downloadsDir = args[2]
    downloadsDir.replace("\"", "")
f = open(downloadsDir)
downloadsJSON = json.load(f)
f.close()

for url in downloadsJSON["downloads"]:
    #checking validity of download links
    if not (url.find("modrinth") == -1):
        if not (len(url.split("/")) == 8):
            raise ValueError("URL invalid, read README.md")
        fileName = url.split("/")[7]
    elif not (url.find("curseforge") == -1):
        if not (len(url.split("/")) == 10):
            raise ValueError("URL invalid, read README.md")
        fileName = url.split("/")[8] + ".jar"
        
    else:
        raise ValueError("Unable to download from non modrinth/curseforge websites, read README.md")
    if not (url.find("download") == -1) or not (url.find("versions") == -1):
        pass
    else:
        raise ValueError("Not a valid download link, read README.md")
    
    downloads[url] = fileName

#make installer.py
f = open(f"installerBase{loader.title()}.py")
installlerBase = f.read()
f.close()

installlerBase = installlerBase.replace("downloads = {}", f"downloads = {downloads}")

f = open("installer.py", "x")
f.write(installlerBase)
f.close()

#package installer.py
os.system("pyinstaller installer.py --onefile")
os.remove("installer.py")
os.remove("installer.spec")
shutil.move("dist/installer.exe", "installer.exe")
shutil.rmtree("dist")
shutil.rmtree("build")