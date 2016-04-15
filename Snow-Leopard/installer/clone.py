print ("This script will create a script that will clone some repos onto your device or machine!")
file = open('git.sh', 'w')
file = open('git.sh', 'a')
file.write('#!/bin/sh\n')
file.write('apt-get update\n')
file.write('apt-get install git\n')
file.write('git clone https://github.com/Ramotion/folding-cell-\n')
file.write('git clone https://github.com/FreeCodeCamp/FreeCodeCamp\n')
file.write('git clone https://github.com/alda-lang/alda\n')
file.write('git clone https://github.com/googlesamples/android-architecture\n')
file.write('git clone https://github.com/vim/vim\n')
file.write('git clone https://github.com/snare/voltron\n')
file.write('read\n')
file.write('exit\n')
file.close()
print ("Finished creating the repo cloning utility!")
#Collections of repos from which I got these links
#https://github.com/showcases/machine-learning
#https://github.com/showcases/design-essentials
#https://github.com/showcases/programming-languages
#https://github.com/trending
