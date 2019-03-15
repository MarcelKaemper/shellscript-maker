import os

print("Welcome to the shellscript construction kit\n")

filename=input("Enter the name of your file >> ")
os.system("touch trash/"+filename+".sh")

operation = ["Echo"]

while(1):
    print("Choose the module you want to add:\n")
    for i, elmnt in enumerate(operation):
        print("["+str(i)+"] "+elmnt+"\n")
    input()
