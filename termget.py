import os
import time
import sys
package = " "
#Imports libraries and sets variables

if len(sys.argv) == 2:
    if sys.argv[1] == "apt-get":
        package = "apt-get"
    elif sys.argv[1] == "pacman":
        package = "pacman"
    elif sys.argv[1] == "xbps":
        package = "xbps"
    elif sys.argv[1] == "dnf":
        package = "dnf"
    elif sys.argv[1] == "zypper":
        package = "zypper"
    elif sys.argv[1] == "eopkg":
        package = "eopkg"

#Checks for command line argument

def clear():
    os.system("clear")
    #Runs 'clear' over shell to clear the screen.

clear()

if package == " ": #Checks for command line argument
    print("Welcome to TermGet. This is a beta, so expect bugs.\n\nPlease choose a package manager\n\n1. apt-get (For Debian, and Debian based systems.)\n2. xbps (For Void Linux, and Void Linux based systems)\n3. dnf (For Fedora, and Fedora based systems)\n4. zypper (For OpenSUSE, and OpenSUSE based systems)\n5. ecopkg (For Solus, and Solus based systems)\n6. pacman (For Arch, and Arch based systems)")
    setup = "True"
    #Sets the variable 'setup' to True
else:
    print("Welcome to TermGet. This is a beta, so expect bugs")
    time.sleep(1)
    clear()
    setup = "False"
    #Sets the variable 'setup' to False

#Asks user which package manager to use

while setup == "True": #Repeats until setup is not true
    user = input() #Asks for user input
    if user == "1":
        setup = "false"
        package = "apt-get" #Sets package manager to apt-get
    elif user == "2":
        setup = "false"
        package = "xbps" #Sets package manager to xbps
    elif user == "3":
        setup = "false"
        package = "dnf" #Sets package manager to dnf
    elif user == "4":
        setup = "false"
        package = "zypper" #Sets package manager to zypper
    elif user == "5":
        setup = "false"
        package = "eopkg" #Sets package manager to eopkg
    elif user == "6":
        setup = "false"
        package = "pacman" #Sets pac(k)age manager to pacman
    else:
        clear()
        print("Error. Invaild package manager")
        time.sleep(1)
        print("\nPlease choose a package manager\n\n1. apt-get (For Debian, and Debian based systems.)\n2. xbps (For Void Linux, and Void Linux based systems)\n3. dnf (For Fedora, and Fedora based systems)\n4. zypper (For OpenSUSE, and OpenSUSE based systems)\n5. ecopkg (For Solus, and Solus based systems)\n6. pacman (For Arch, and Arch based systems)")
        #Sets up the package manager

    clear()

while True: #Starts a loop
    clear()
    print("Please choose an action\n\n1. Search for packages\n2. Install an application\n3. Remove an application\n4. Update all packages\n5. Update Repo\n6. Clean\n7. Credits\n8. Exit")
    user = input() #Asks for user input

    if user == "1": #Search
        clear()
        user = input("Please enter search query: ")
        print(" ")
        if package == "apt-get":
            os.system("apt-cache search " + user)
        elif package == "pacman":
            os.system("pacman -Sy " + user)
        elif package == "xbps":
            os.system("xbps-query -Rs " + user)
        elif package == "dnf":
            os.system("dnf search " + user)
        elif package == "zypper":
            os.system("zypper search " + user)
        elif package == "eopkg":
            os.system("eopkg search " + user)
        input("\nPress enter to continue")

    if user == "2": #Install
        clear()
        user = input("Please enter which package(s) to install: ")
        print("")

        if package == "apt-get":
            os.system("sudo apt-get install " + user)
        if package == "pacman":
            input("Which package manager would you like to use?\n\n1. pacman\n2. yaourt\n")
            if user == "1":
                os.system("sudo pacman -S " + user)
            if user == "2":
                os.system("sudo yaourt -S " + user)
        if package == "xbps":
            os.system("sudo xbps-install " + user)
        if package == "dnf":
            os.system("sudo dnf install " + user)
        if package == "zypper":
            os.system("sudo zypper install " + user)
        if package == "eopkg":
            os.system("sudo eopkg install " + user)
        input("\nPress enter to continue")

    if user == "3": #Remove
        clear()
        user = input("Please enter which package(s) to remove: ")
        print("")

        if package == "apt-get":
            user = input("How will you like to remove the package?\n\n1. remove, removes just the package (faster)\n2. purge, removes the package, and all it's configuration files (saves space)")
            clear()
            if user == "1":
                os.system("sudo apt-get remove " + user)
            if user == "2":
                os.system("sudo apt-get purge " + user)
        if package == "pacman":
            os.system("sudo pacman -Rs " + user)
        if package == "xbps":
            os.system("sudo xbps-remove " + user)
        if package == "dnf":
            os.system("sudo dnf remove " + user)
        if package == "zypper":
            os.system("sudo zypper remove " + user)
        if package == "eopkg":
            os.system("sudo eopkg remove " + user)
        input("\nPress enter to continue")

    if user == "4": #Updates Packages
        clear()
        print("\n")
        if package == "apt-get":
            os.system("sudo apt-get upgrade")
            os.system("sudo apt-get dist-upgrade")
        if package == "pacman":
            os.system("sudo pacman -Syu")
        if package == "xbps":
            os.system("sudo xbps-install -Su")
        if package == "dnf":
            os.system("sudo dnf upgrade")
            os.system("sudo dnf distro-sync")
        if package == "zypper":
            os.system("sudo zypper update zypper up")
            os.system("sudo zypper dup")
        if package == "eopkg":
            os.system("sudo eopkg upgrade")
        input("\nPress enter to continue")

    if user == "5": #Updates Repo
        clear()
        print("\n")
        if package == "apt-get":
            os.system("sudo apt-get update")
        elif package == "pacman":
            os.system("sudo pacman -Sy")
        elif package == "xbps":
            os.system("sudo xbps-install -S")
        elif package == "dnf":
            os.system("sudo dnf clean expire-cache && dnf check-update")
        elif package == "zypper":
            os.system("sudo zypper refresh zypper ref")
        elif package == "eopkg":
            os.system("sudo eopkg ur")
        input("\nPress enter to continue")

    if user == "6": #Cleans

        clear()

        if package == "apt-get":
            os.system("sudo apt-get autoremove")
            os.system("sudo apt-get clean")
        if package == "pacman":
            os.system("sudo pacman -Qdtq | pacman -Rs -")
            os.system("sudo pacman -Sc")
        if package == "xbps":
            os.system("sudo xbps-remove -o")
            os.system("sudo xbps-remove -O")
        if package == "dnf":
            os.system("sudo dnf autoremove")
            os.system("sudo dnf clean all")
        if package == "zypper":
            os.system("sudo zypper rm -u")
            os.system("sudo zypper clean")
        if package == "eopkg":
            os.system("sudo eopkg delete-cache")
            os.system("sudo eopkg remove-orphans")
        input("\nPress enter to continue")

    if user == "7": #Credits
        print("TermGet was created by:\n- PizzaLovingNerd (main developer)\n- SudoLinux")
        time.sleep(3)
        #If you contribute, please add your name.

    if user == "8": #Quit
        quit()