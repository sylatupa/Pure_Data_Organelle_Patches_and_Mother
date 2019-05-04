# Run this script on start-up, on your Raspberry Pi.
# This will automatically start Pure Data so you can run Pure Data headless on a Raspberry Pi.

# Here are some example lines that you may want to have for your shell script.
# You will need to edit the path.
# Order is important, first start the patch you want and then the mother patch. Opening the mother patch last sends a load bang to the other open patches, setting some initial values.


#sudo pd -nogui -audiooutdev 3,4 -audioindev 3,4 /home/pi/Tools_And_Such/Patches_Working/main_final_version.pd
#sudo pd -nogui -audioindev 3,4 -audiooutdev 3,4  /home/pi/Tools_And_Such/Patches_Working/C_DelayAuto/main_final_version.pd &
#sudo pd -nogui /home/pi/GIT_LOCAL_WORKING/A_PURE_DATA/Patches/mother-desktop-raspbad-kordbot.pd

sudo pd $HOME/Digital-Culture-Sound-Client/Pure_Data_Patches/E_Basic_Poly/main.pd &
sudo pd -nogui /home/pi/GIT_LOCAL_WORKING/A_PURE_DATA/Patches/mother-desktop-raspad.pd	
