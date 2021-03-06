import os
import re

print("Welcome to the shellscript construction kit\n")

# Appends <string> to <filename>
def append(filename, string):
    with open(filename,"a") as w:
        w.write(string+"\n")

def clear():
    print("\n"*100)

def echo():
    choice = input("[1] Echo text\n[2] Echo variable\n>> ")
    if(choice == "1"):
        append(path, "echo "+input("Text to echo: "))
    elif(choice == "2"):
        variables = findVar(path)
        for i in range(len(variables[0])):
            print("["+str(i+1)+"] "+variables[0][i])
        append(path, "echo $"+variables[0][int(input("Choose a variable\n>> "))-1])

def variable():
    name = input("Name:")
    value = input("Value:")
    if ' ' in value:
        value="\""+value+"\""
    append(path, name+"="+value)

def ifstatement():
    types = ["Variable comparison"]
    statement = ""

    print("Choose the type of condition\n")

    for i, elmnt in enumerate(types,start=1):
        print("["+str(i)+"] "+elmnt+"\n")

    choice = input("Type of condition:\n>> ")

    if choice == "1":
        variables = findVar(path)
        for i in range(len(variables[0])):
            print("["+str(i+1)+"] "+variables[0][i])
        variable = variables[0][int(input("Choose a variable:\n>> "))-1]
        compareTo = input("What do you want to compare "+variable+" to?\n>> ")
        statement += "if [ \"$"+variable+"\" = "+compareTo+" ]\nthen"
        append(path,statement)
        append(path,"fi")

    # consequence = input("If condition is true\n>> ")

    

def custom():
    append(path, input("Enter the line you want to add:\n>> "))

# Function that returns a list of all existing variables in <filename> and their values in this format:
# [[name1,name2],[value1,value2]]
def findVar(filename):
    variables = [[],[]]
    pattern=r'^(\S+) *[=] *"*([^"\n]+)"*;*[\n]*$'
    with open(filename,"r") as w:
        for element in w.readlines():
            obj = re.match(pattern, element)
            if obj != None:
                variables[0].append(obj.group(1))
                variables[1].append(obj.group(2))
    return variables


path=input("Enter the name of your file >> ")+".sh"

os.system("touch "+path)
os.system("chmod +x "+path)
append(path, "#!bin/shell\n")

modules = ["Echo", "Variable", "If Statement", "Custom", "Exit"]


while(1):
    clear()
    print("Choose the module you want to add:\n")
    for i, elmnt in enumerate(modules,start=1):
        print("["+str(i)+"] "+elmnt+"\n")

    module = input("Choose module: ")
    # Converting to lowercase, removing whitespaces and calling function
    eval(modules[int(module)-1].lower().replace(" ","")+"()")
