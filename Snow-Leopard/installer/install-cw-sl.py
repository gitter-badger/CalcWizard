#This software is licensed under the GNU GPL v3.0.

import os

import time

print ("This script will install CalcWizard Snow Leopard on your system!")

location = raw_input("Type the full path to the installation directory here: ")

ktc = ("Press any key to exit the program!")

os.system("cd ../")

os.system("cd ../")

os.system("mv CalcWizard " + str(location))

desktop = raw_input("Type the full path to your desktop here: ")

os.system("cd " + str(desktop))

startsh = open("CalcWizard-starter.sh", "w")

startsh = open("CalcWizard-starter.sh", "a")

startsh.write("#!/bin/bash\n")

startsh.write("cd " + str(location) + "\n")

startsh.write("cd CalcWizard/Snow-Leopard/program\n")

startsh.write("python snowleopard.py\n")

startsh.write(str(ktc) + "\n")

startsh.write("rea\n")

startsh.write("exit\n")

startsh.close()

print ("Alle files and drectories have been generated!")

print ("The installation has been completed!")

print ("To start CalcWizard Snow Leopard, open a command prompt on your desktop")

print ("and type 'bash start.sh' to start the program!")

exit = raw_input("Do you want to exit?(y/n)")

if exit == "y":
  print ("The program will exit in 5 seconds.")
  time.sleep(5)
  exit()
elif exit == "n":
  print ("Exiting anyway!")
  time.sleep(5)
  exit()
else:
  print ("Exiting...")
  time.sleep(5)
  exit()
