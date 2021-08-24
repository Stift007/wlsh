import os

def menu():
    os.system("clear")
    print("WLED - WorstLinuxEDitor")
    print("-"*20)
    print("1: Create a File")
    print("2: Load a File")
    print("3: Version, Help and Changelog")
    print("4: Quit WLED")
    try:
        cm = int(input("> "))
        if cm == 1:new()
        elif cm==2:load()
        elif cm==3:changelog()
        elif cm==4:return
        menu()
    except:
        menu()
        
def mainloop(path):
    with open(path,"r+") as f:
        content = f.read()
    while True:
        os.system("clear")
        print(content)
        text = input("> ")
        if text == "w":
            with open(path,"w+") as f:
                f.write(content)

        elif text == "wq":
            with open(path,"w+") as f:
                f.write(content)
            return 0

        
        elif text == "q":
            return 0


        elif text == "m":
            content = ""
            menu()

        elif text == "wm":
            with open(path,"w+") as f:
                f.write(content)
            content = ""
            menu()

            
            

        else:
            content += f"\n{text}"

def load():
    __path = input("path/filename of File: ")
    mainloop(__path)

def new():
    __path = input("path/filename of new File: ")
    with open(__path,"w") as f:
        f.write("   ")
    mainloop(__path)

def changelog():
    os.system("clear")
    print("WLED 2.4")
    print("WLED (WorstLinuxEDitor) is a Text Editor that comes with")
    print("The WLSH (WorstLinuxShell). The Problem is, that you can only \nwrite Files, not EDIT them.")
    print("To Use the program properly, you have to use commands.")
    print("The Commands are:")
    print("w: Write the Changes to File")
    print("m: Discard Unsaved changes and return to menu")
    print("wm: Write Changes and return to menu")
    print("q: Quit WLED and discard changes")
    print("wq: Quit WLED and Save the Changes")
    print("-----------------------------------------------------------------------")
    input("Press enter to return to menu")
    menu()

def main():
    menu()
