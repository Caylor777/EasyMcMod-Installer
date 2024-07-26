# EasyMcMod Generator
Create a .exe to easily install minecraft mods to the .minecraft/mods folder  

## Installation
1.zip or clone the github repository  
2.Ensure python is installed (worked on 3.11.5)  
3.pip install -r requirements. txt  

## Usage
1.Put download links in the "downloads.json" file (only accepts modrinth/curseforge links)  
  *for modrinth, under the versions tab "copy link address" of the download icon on the indended version  
  *for cureforge you must wait for the 5 seconds and "copy link address" for the "try again" button  
2.right click on empty space in the folder and select "open in terminal"  
3.In the terminal windows type "python main.py <"forge"/"fabric"> <file path to "download.json">  
  *2ed argument(<file path to "download.json">) is not required and if not given the program will assume that the "downloads.json" is in the same folder as "main.py"  

## Dependencies
python  
pyinstaller  

## Contributing
https://github.com/Caylor777

## License
MIT License

## Contact
https://github.com/Caylor777/AutoShorts
