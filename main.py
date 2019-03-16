import os

print("Welcome to the shellscript construction kit\n")

def append(filename, string):
    with open(filename,"a") as w:
        w.write(string+"\n")

def echo():
    choice = input("[1] Echo text\n[2] Echo variable\n>>")
    if(choice == "1"):
        append(path, "echo "+input("Text to echo: "))
    elif(choice == "2"):
        append(path, "echo $"+input("Variable name: "))


def variable():
    name = input("Name:")
    value = input("Value:")
    if ' ' in value:
        value="\""+value+"\""
    append(path, name+"="+value)

path=input("Enter the name of your file >> ")+".sh"

os.system("touch "+path)
os.system("chmod +x "+path)
append(path, "#!bin/shell\n")

modules = ["Echo", "Variable", "If/Else", "Exit"]

while(1):
    print("Choose the module you want to add:\n")
    for i, elmnt in enumerate(modules,start=1):
        print("["+str(i)+"] "+elmnt+"\n")

    module = input("Choose module: ")
    eval(modules[int(module)-1].lower()+"()")
