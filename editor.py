import bpy 
from bpy.props import StringProperty, BoolProperty, EnumProperty 
from bpy.types import NodeTree,NodeSocket


class CustomNodeTree(bpy.types.NodeTree):
    """A custom node editor"""
    bl_idname = 'CustomNodeTreeType'
    bl_label = 'Custom Nodes'
    bl_icon = 'UGLYPACKAGE'

def register():
    bpy.utils.register_class(CustomNodeTree)

def unregister():
    bpy.utils.unregister_class(CustomNodeTree)