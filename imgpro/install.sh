#!/bin/sh

APP_PATH='/usr/share/applications'
ICON_PATH='/usr/share/pixmaps'
SRC_PATH='/usr/share/imgpro'
BIN_PATH='/usr/bin'

mkdir -p ./pkg/$SRC_PATH

cp -f ./src/*.py $SRC_PATH/
mkdir $SRC_PATH/backend
cp -f ./src/backend/*.py $SRC_PATH/backend/
mkdir $SRC_PATH/ui
cp -f ./src/ui/*.py $SRC_PATH/ui/

cp -f ./src/image/icon.png $ICON_PATH/imgpro.png
cp -f ./src/imgpro.desktop $APP_PATH/
ln -s $SRC_PATH/imgpro.py $BIN_PATH/imgpro

echo "Done."
echo 'Execute \"imgpro\" and have fun'
