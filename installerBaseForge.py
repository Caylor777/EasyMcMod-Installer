import os, shutil, webbrowser, time
import urllib3.poolmanager

downloads = {}

#open browser link to download loader
print("opeaning browser")
time.sleep(0.5)
webbrowser.open("https://files.minecraftforge.net/net/minecraftforge/forge/index_1.20.2.html", new=2)
print("")
print("Download the required version of forge and run the installer")
print("*WHEN FORGE OPENS A NEW TAB WAIT 5 SECONDS THEN PRESS SKIP IN THE TOP RIGHT*")
print("press enter once the installer has finished")
input()

for url in downloads:
    #download links
    print(f"downloading {downloads[url]}")
    c = urllib3.PoolManager()
    with c.request('GET',url, preload_content=False) as resp, open(downloads[url], 'wb') as out_file:
        shutil.copyfileobj(resp, out_file)
    resp.release_conn()
    print("downloaded")
    
    print(f"moving {downloads[url]}")
    #move links to mods folder
    os.replace(downloads[url], f"{os.getenv('APPDATA')}\\.minecraft\\mods\\{downloads[url]}")
    print("moved")
    
print("complete")