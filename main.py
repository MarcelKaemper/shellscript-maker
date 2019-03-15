import os

print("Welcome to the shellscript construction kit\n")

def append(filename, string):
    with open(filename,"a") as w:
        w.write(string)

path=input("Enter the name of your file >> ")+".sh"

os.system("touch "+path)
os.system("chmod +x "+path)
append(path, "#!bin/shell\n")

modules = ["Echo"]

while(1):
    print("Choose the module you want to add:\n")
    for i, elmnt in enumerate(modules,start=1):
        print("["+str(i)+"] "+elmnt+"\n")
    module = input("Module:")
    if(module == "1"):
        append(path, "echo "+input("Text to echo:"))
