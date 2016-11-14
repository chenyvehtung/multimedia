#!/bin/sh

INSTALL_PATH="/usr/share/uniqimg"
BIN_PATH="/usr/bin"
ICON_PATH="/usr/share/pixmaps"
APP_PATH="/usr/share/applications"

rm -rf $INSTALL_PATH
rm -f $BIN_PATH/uniqimg
rm -f $APP_PATH/uniqimg.desktop
rm -f $ICON_PATH/uniqimg.png

echo "Done."
