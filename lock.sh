#!/bin/bash

# Установите путь к вашему изображению
BACKGROUND="/home/luxy/Downloads/hananuki-gorge-japan-scenic-spot-suspended-bridge-thick-3840x2160-7466.jpg"

# Установите фон с помощью feh
feh --bg-scale "$BACKGROUND"

# Запустите i3lock
i3lock -i "$BACKGROUND"
