import os, shutil, json, sys, webbrowser
import urllib3.poolmanager

#collect args
args = sys.argv
if len(sys.argv) < 2:
    raise IndexError("1 argument must be passed")
if args[1] == "fabric":
    c = urllib3.PoolManager()
    with c.request('GET',"https://maven.fabricmc.net/net/fabricmc/fabric-installer/1.0.1/fabric-installer-1.0.1.jar", preload_content=False) as resp, open("fabric-installer.jar", 'wb') as out_file:
        shutil.copyfileobj(resp, out_file)
    resp.release_conn()
    os.system("fabric-installer.jar")
    os.remove("fabric-installer.jar")
elif args[1] == "forge":
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    webbrowser.open
    webbrowser.open("https://files.minecraftforge.net/net/minecraftforge/forge/index_1.20.2.html", new=2)
    print("Download the required version of forge and run the installer")
    print("*WHEN FORGE OPENS A NEW TAB WAIT 5 SECONDS THEN PRESS SKIP IN THE TOP RIGHT*")
    print("press enter once the installer has finished")
    input()
else:
    raise TypeError(f"\"{args[1]}\" is not a valid argument, must be \"forge\" or \"fabric\"")

#read fiiles to download
downloadsDir = "downloads.json"
if len(args) < 2:
    downloadsDir = args[2]
    downloadsDir.replace("\"", "")
f = open(downloadsDir)
downloads = json.load(f)
f.close()

#download files in downloads.json
for url in downloads["downloads"]:
    #checking validity of download links
    if not (url.find("modrinth") == -1):
        try:
            fileName = url.split("/")[7]
            if len(url.split("/")) > 8:
                raise ValueError("URL invalid, read README.md")
        except:
            raise ValueError("URL invalid, read README.md")
    elif not (url.find("curseforge") == -1):
        try:
            fileName = url.split("/")[8] + ".jar"
            url.split("/")[9]
            if len(url.split("/")) > 10:
                raise ValueError("URL invalid, read README.md")
        except:
            raise ValueError("URL invalid, read README.md")
    else:
        raise ValueError("Unable to download from non modrinth/curseforge websites, read README.md")
    
    if not (url.find("download") == -1) or not (url.find("versions") == -1):
        pass
    else:
        raise ValueError("Not a valid download link, read README.md")
    
    #download links
    c = urllib3.PoolManager()
    with c.request('GET',url, preload_content=False) as resp, open(fileName, 'wb') as out_file:
        shutil.copyfileobj(resp, out_file)
    resp.release_conn()
    
    #move links to mods folder
    os.replace(fileName, f"{os.getenv('APPDATA')}\\.minecraft\\mods\\{fileName}")
    