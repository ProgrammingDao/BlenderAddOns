# BlenderAddOns

Modules for blender add ons.

-------------------------------------

Installation
-------------

- Follow the steps to build blender locally : 
https://wiki.blender.org/wiki/Building_Blender
- Select the python interpreter where bpy has been installed as your project's interpreter in an IDE such as pycharm. 
Usually under build_darwin/bin/Blender.app/Contents/Resources/[Version]/python/bin/python3.9 (for mac)
- Run pip install requirements.txt to install the stub interface for bpy and other modules.
- To install the addons, follow the usual practice as defined at
https://docs.blender.org/manual/en/latest/advanced/scripting/addon_tutorial.html#install-the-add-on
- Start using the installed addons by selecting them under Edit -> Menu Search ...

Adding new Addon
-----------------

- create new python script under src/addons.
- write the addon code.
- if the addon doesn't contain module imports besides the one for bpy, then you can just import the python file.
- otherwise, zip the python file and install the python file instead of the python file.

Notes:

- bl_info shouldn't have its type specified. The addon won't be installed if it does.

Debugging
-----------

Pycharm support is very limited here and the best way is to use visual studio with the excellent extension by Jacques Lucke that can be found at : https://marketplace.visualstudio.com/items?itemName=JacquesLucke.blender-development

To debug the addon, run: Blender: Build and Start. Can be accessed with ctrl + shift + p.

Status
-------

Dropped until blender python package is properly released, it becomes easier to test and maintain the code.
