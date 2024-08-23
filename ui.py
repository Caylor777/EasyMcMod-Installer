import os, time

class ui:
    def selectInstaller() -> str:
        installerList = []
        for path in os.listdir():
            if not path.find("installer") == -1:
                installerList.append(path)
                
        if len(installerList) < 1:
            print("No installers found")
            time.sleep(3)
            raise Exception("No installers found")
        elif len(installerList) == 1:
            return installerList[0]
        
        for i in range (0, len(installerList)):
            print(f"{i + 1}. {installerList[i]}")
            
        answer = input("Select one of the listed installers: ")
        answer = int(answer)
        
        if answer > len(installerList) or answer < 1:
            ui.selectInstaller()
        else:
            return installerList[answer - 1]
        
    
    def verifyModsPath(path) -> str:
        print("-------------------")
        print(f"is this the path to your minecraft mods folder? {path}")
        answer = input("y/N: ")
        if answer == "y":
            return path
        elif answer == "N":
            return input("Enter correct file path: ")
        else:
            ui.verifyModsPath(path)
    
    def managePreExistingMods(path) -> bool:
        print("-------------------")
        print(f"What do you want to do with these files alreay in your mods folder:")
        print("\n".join(os.listdir(path)))
        print()
        answer = input("1. Delete files in mods folder\n2. copy files to a new folder\n")
        if answer == "1":
            return True
        elif answer == "2":
            return False
        else:
            ui.managePreExistingMods(path)