import os, shutil
import urllib3.poolmanager

downloads = {}

#download and run fabric loader
print("downloading fabric-installer.jar")
c = urllib3.PoolManager()
with c.request('GET',"https://maven.fabricmc.net/net/fabricmc/fabric-installer/1.0.1/fabric-installer-1.0.1.jar", preload_content=False) as resp, open("fabric-installer.jar", 'wb') as out_file:
    shutil.copyfileobj(resp, out_file)
resp.release_conn()
print("downloaded")
print("running fabric-installer.jar")
os.system("fabric-installer.jar")
print("removing fabric-installer.jar")
os.remove("fabric-installer.jar")

for url in downloads:
    #download links
    print(f"downloading {downloads[url]}")
    c = urllib3.PoolManager()
    with c.request('GET',url, preload_content=False) as resp, open(downloads[url], 'wb') as out_file:
        shutil.copyfileobj(resp, out_file)
    resp.release_conn()
    print("downloaded")
    
    #move links to mods folder
    print(f"moving {downloads[url]}")
    os.replace(downloads[url], f"{os.getenv('APPDATA')}\\.minecraft\\mods\\{downloads[url]}")
    print("moved")
    
print("complete")