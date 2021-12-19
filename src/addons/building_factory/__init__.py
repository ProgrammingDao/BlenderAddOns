"""Addon to provide a factor to ease the design and creation of buildings."""

import bpy

bl_info = {
    "name" : "Building Factory",
    "author" : "ProgrammingDao",
    "description" : "",
    "blender" : (3, 0, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}


class BuildingFactory(bpy.types.Operator):
    """Building Factory"""  # Use this as a tooltip for menu items and buttons.
    bl_idname = "generic.building_factory"  # Unique identifier for buttons and menu items to reference.
    bl_label: str = "Building Factory"  # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.

    def execute(self, context):  # execute() is called when running the operator.

        bpy.ops.mesh.primitive_plane_add(size=1.0, align="WORLD")

        return {'FINISHED'}  # Lets Blender know the operator finished successfully.


def menu_func(self, context):
    self.layout.operator(BuildingFactory.bl_idname)


def register():
    bpy.utils.register_class(BuildingFactory)
    bpy.types.VIEW3D_MT_mesh_add.append(menu_func)  # Adds the new operator to an existing menu.


def unregister():
    bpy.utils.unregister_class(BuildingFactory)


# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()
