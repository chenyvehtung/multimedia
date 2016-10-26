#!/bin/sh

APP_PATH='usr/share/applications'
ICON_PATH='usr/share/pixmaps'
SRC_PATH='usr/share/uniqimg'

rm -rf ./pkg/
rm -rf ./*.deb
mkdir -p ./pkg/$APP_PATH
mkdir -p ./pkg/$ICON_PATH
mkdir -p ./pkg/$SRC_PATH
cp -rf ./DEBIAN ./pkg/

cp -f ./src/*.py ./pkg/$SRC_PATH/
mkdir ./pkg/$SRC_PATH/backend
cp -f ./src/backend/*.py ./pkg/$SRC_PATH/backend/
mkdir ./pkg/$SRC_PATH/ui
cp -f ./src/ui/*.py ./pkg/$SRC_PATH/ui/

cp -f ./src/image/icon.png ./pkg/$ICON_PATH/uniqimg.png
cp -f ./src/uniqimg.desktop ./pkg/$APP_PATH/

dpkg -b ./pkg uniqimg_0.1.2_all.deb
