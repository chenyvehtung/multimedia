# UNIQIMG (Unique Image)

![icon](/screenshots/icon.png)

A simple application for removing similar images in the selected path. Based on PyQt4


## Install

The project provides with a debain package, which is packed up under Ubuntu 14.10
Use the following command to install it

```sh
sudo dpkg -i uniqimg_0.1.0_all.deb
sudo apt -f install
```

and after that, you would see uniqimg icon in your Applications, click the icon to run it.
or you can run it from terminal, use the following command

```sh
uniqimg
```

## Dependency

For developer, the following package should be installed.

* python2.7
* python-qt4
* python-numpy
* python-scipy
* python-pil

you can install them by using the following command

```sh
sudo apt install python2.7 python-qt4 python-numpy python-scipy python-pil
```

## Build Package

Run the following command, and it would generate a new debian package based on the code inside the `./src` folder.

```sh
sh mkpkg.sh
```

## Intruction

1. Click the "Open Folder" button to select a folder where you want to search for duplicate images.
2. Select "hash algorithm" and "search depth" in the toolbar.
3. Click "Search" button to search for duplicate images.
4. The results would be shown on the lower part, in which each kind of duplicate images will be stored in a folder.
5. Click a folder to open the detail dialog, where you could see all of the duplicate images.
6. Check some images you want to remove, a preview of the selected image will be presented on the right hand side.
7. Click "Remove" button to remove the selected images. And that's it.

## Screenshots

* Homepage

![](/screenshots/1.jpeg)

* Result page

![](/screenshots/2.jpeg)

* Similar image detail page

![](/screenshots/3.jpeg)
![](/screenshots/4.jpeg)

* Remove image dialog

![](/screenshots/5.jpeg)
