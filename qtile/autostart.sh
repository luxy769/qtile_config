#!/bin/bash

#keyboard layout
#setxkbmap us,ru -option grp:win_space_toggle
setxkbmap us,ru -option grp:caps_toggle
#wallpaper
feh --bg-scale ~/Downloads/hananuki-gorge-japan-scenic-spot-suspended-bridge-thick-3840x2160-7466.jpg

#touchpad left click
xinput set-prop 9 "libinput Tapping Enabled" 1 &
