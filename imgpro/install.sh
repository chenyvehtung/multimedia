#!/bin/sh

APP_PATH='/usr/share/applications'
ICON_PATH='/usr/share/pixmaps'
SRC_PATH='/usr/share/uniqimg'
BIN_PATH='/usr/bin'

mkdir -p ./pkg/$SRC_PATH

cp -f ./src/*.py $SRC_PATH/
mkdir $SRC_PATH/backend
cp -f ./src/backend/*.py $SRC_PATH/backend/
mkdir $SRC_PATH/ui
cp -f ./src/ui/*.py $SRC_PATH/ui/

cp -f ./src/image/icon.png $ICON_PATH/uniqimg.png
cp -f ./src/uniqimg.desktop $APP_PATH/
ln -s $SRC_PATH/uniqimg.py $BIN_PATH/uniqimg

echo "Done."
echo 'Execute \"uniqimg\" and have fun'
