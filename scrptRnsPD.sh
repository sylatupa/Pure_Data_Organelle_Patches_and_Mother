#sudo pd -nogui -audiooutdev 3,4 -audioindev 3,4 /home/pi/Tools_And_Such/Patches_Working/main_final_version.pd
sudo pd -nogui -audioindev 1,2 -audiooutdev 1,2 $HOME/Digital-Culture-Sound-Client/Pure_Data_Patches/E_Basic_Poly/main.pd &
sudo pd -nogui -audioindev 1,2 -audiooutdev 1,2 $HOME/Digital-Culture-Sound-Client/Pure_Data_Patches/mother-desktop-raspad-kordbot.pd
