bl_info = {
    "name": "flatcamera",
    "blender": (3, 0, 0),
    "category": "Object",
}

import bpy
from bpy.types import Operator
from bpy.props import BoolProperty
import math

class OBJECT_OT_add_custom_camera(Operator):
    bl_idname = "object.add_custom_camera"  # Unique identifier
    bl_label = "Flat Camera"               # Display name in UI
    bl_description = "Add a flat camera"
    bl_options = {'REGISTER', 'UNDO'} 

    is_ortho: BoolProperty(
        name="Orthographic",
        description="Enable orthographic mode for the camera",
        default=False,
    )

    def execute(self, context):
        """
        This method defines what happens when the operator is executed.
        """
        # Add a new camera
        bpy.ops.object.camera_add(
            align='WORLD',
            location=(0, 0, 0),
            rotation=(math.radians(90), 0, math.radians(90))
        )

        camera_obj = context.object  # Get the newly created camera

        # Set camera to orthographic if enabled
        if self.is_ortho:
            camera_obj.data.type = 'ORTHO'

        return {'FINISHED'}  # Indicate successful execution

# Menu function to add the operator to the Add > Camera menu
def menu_func(self, context):
    self.layout.operator(OBJECT_OT_add_custom_camera.bl_idname, text="Flat Camera")

# Register and unregister functions
def register():
    bpy.utils.register_class(OBJECT_OT_add_custom_camera)
    bpy.types.VIEW3D_MT_camera_add.append(menu_func)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_add_custom_camera)
    bpy.types.VIEW3D_MT_camera_add.remove(menu_func)

# Entry point for running the script
if __name__ == "__main__":
    register()
