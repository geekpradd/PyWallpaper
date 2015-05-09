##PyWallpaper: Change Wallpaper from Python 

PyWallpaper is a cross platform Python module to change wallpapers across different platforms.

The module uses ctypes and subprocess to work and the code is cross platform

##Installation

Use pip

```
pip install PyWallpaper
```

##Usage

There is a single function, change_wallpaper

Example:

```python
from PyWallpaper import change_wallpaper
change_wallpaper("C:/Users/Pradipta/Pictures/Misc/city.jpg")
```

You have to use `/` in place of `\` in Windows (or `\\`) because of Python restrictions

##Limitations

1. Python 3 support in Windows (To-Do)
2. Linux support works only on GNOME, Unity and Cinnamon Desktops

##About

Created by Pradipta. Copyright 2015. MIT Licensed.