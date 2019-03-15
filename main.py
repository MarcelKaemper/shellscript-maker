import os

print("Welcome to the shellscript construction kit\n")

def append(filename, string):
    with open(filename,"a") as w:
        w.write(string)

path="trash/"+input("Enter the name of your file >> ")+".sh"

os.system("touch "+path)
append(path, "Howdy\n")

operation = ["Echo"]

while(1):
    print("Choose the module you want to add:\n")
    for i, elmnt in enumerate(operation,start=1):
        print("["+str(i)+"] "+elmnt+"\n")
    input()
