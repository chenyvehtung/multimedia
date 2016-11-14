#!/bin/sh

INSTALL_PATH="/usr/share/imgpro"
BIN_PATH="/usr/bin"
ICON_PATH="/usr/share/pixmaps"
APP_PATH="/usr/share/applications"

rm -rf $INSTALL_PATH
rm -f $BIN_PATH/imgpro
rm -f $APP_PATH/imgpro.desktop
rm -f $ICON_PATH/imgpro.png

echo "Done."
