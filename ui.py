import os

class ui:
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
        answer = input("1. Delete files in mods folder\n2. copy files to a folder in the program folder")
        if answer == "1":
            return True
        elif answer == "2":
            return False
        else:
            ui.managePreExistingMods(path)