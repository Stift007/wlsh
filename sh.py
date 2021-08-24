from io import IncrementalNewlineDecoder
import os,sys,requests,json
from pprint import pprint
from editor.edit import main

while True:
    cmd = input(f"root@wlsh:{os.getcwd()}>")
    if cmd.startswith("cd"):
        args = cmd.split(" ")
        del args[0]
        try:
            os.chdir(" ".join(args))
        except Exception as e:
            print(f"Error: {e}")

    if cmd.startswith("mkdir"):
        args = cmd.split(" ")
        del args[0]
        try:
            os.mkdir(" ".join(args))
        except Exception as e:
            print(f"Error: {e}")

    elif cmd == "ls":
        print(" ".join(os.listdir(os.getcwd())))

    elif cmd == "exit":
        sys.exit(0)

    elif cmd == "clear":
        os.system("clear")


    elif cmd.startswith("requests"):
        argv = cmd.split(" ")
        try:
            if argv[1] == "get":
                try:
                    if argv[3] == "-h":
                        headers = json.loads(argv[4])
                        r = requests.get(argv[2], headers=headers)

                    else:
                        r = requests.get(argv[2])
                except IndexError:
                    r = requests.get(argv[2])
                print(f"Response: {r.status_code}")
                print("JSON-Like Response:")
                try:
                    pprint(r.json())
                except:
                    print("None")
                print("Raw Text:")
                print(r.text)
        except:
            pass

    elif cmd.startswith("sys "):
        try:
            com,*args = cmd.split(" ")
            os.system(" ".join(args))
        except:
            print("Please use a Command")
    
    elif cmd.startswith("wled"):
        main()

    elif cmd.startswith("cat"):
        try:
            com,*file = cmd.split(" ")
            try:
                print(open(" ".join(file),"r").read())
            except Exception as ex:
                print(ex)
        except IndexError:
            print("Please specify a file!")

        else:
            pass

    else:
        print("Bad Command")

    