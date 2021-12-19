
"""
Addon to move selected object by 1 unit across the X-axis.
Addon has been copied from Blender documentation.
"""

from typing import Set
import bpy

bl_info = {
    "name" : "Move X Axis",
    "author" : "Blender",
    "description" : "",
    "blender" : (3, 0, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Object"
}

class ObjectMoveX(bpy.types.Operator):
    """My Object Moving Script"""  # Use this as a tooltip for menu items and buttons.
    bl_idname: str = "object.move_x"  # Unique identifier for buttons and menu items to reference.
    bl_label: str = "Move X by One"  # Display name in the interface.
    bl_options: Set[str] = {'REGISTER', 'UNDO'}  # Enable undo for the operator.

    def execute(self, context):  # execute() is called when running the operator.

        # The original script
        scene = context.scene
        for obj in scene.objects:
            obj.location.x += 1.0

        return {'FINISHED'}  # Lets Blender know the operator finished successfully.


def menu_func(self, context):
    self.layout.operator(ObjectMoveX.bl_idname)


def register():
    bpy.utils.register_class(ObjectMoveX)
    bpy.types.VIEW3D_MT_object.append(menu_func)  # Adds the new operator to an existing menu.


def unregister():
    bpy.utils.unregister_class(ObjectMoveX)


# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()

