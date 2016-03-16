#This software is licensed under the GNU GPL v3.0.

import os

import time

print ("This script will install CalcWizard Snow Leopard on your system!")

location = raw_input("Type the full path to the installation directory here: ")

ktc = ("Press any key to exit the program!")

os.system("cd ../")

os.system("cd ../")

os.system("mv CalcWizard " + str(location))

startsh = open("CalcWizard-starter.sh", "w")

startsh = open("CalcWizard-starter.sh", "a")

startsh.write("#!/bin/bash")

startsh.write("cd" + str(location))

startsh.write("cd CalcWizard/Snow-Leopard/program")

startsh.write("python snowleopard.py")

startsh.write(str(ktc))

startsh.write("read")

startsh.write("exit")

