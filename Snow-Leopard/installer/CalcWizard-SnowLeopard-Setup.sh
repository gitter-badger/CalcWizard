#This software is licensed under the GNU GPL v3.0.
echo "CalcWizard for Linux"
echo "Welcome to the Snowleopard Release of"
echo "CalcWizard for Linux!"
echo "Installing dependemcies..."
echo "Press any key to continue!"
read
echo "Updating package lists..."
sudo apt-get update
echo "...done."
echo "Press any key to continue!"
read
echo "Installing Python..."
sudo apt-get install python
echo "...done."
echo "Press any key to continue!"
read
echo "Updating package lists..."
sudo apt-get update
echo "...done."
echo "Press any key to continue!"
read
echo "Installing Git..."
sudo apt-get install git
echo "...done."
echo "Press any key to continue!"
read
echo "All dependencies have been installed!"
echo "Starting second part of installation!"
echo "Press any key to continue!"
read
echo "Cloning repos to current directory.."
git clone https://github.com/al3xv3gas/CalcWizard.git
cd CalcWizard
cd installerscripts
python install-cw-sl.py
echo ("Press any key to exit the program!")
read
exit
