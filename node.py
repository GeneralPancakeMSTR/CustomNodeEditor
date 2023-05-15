import bpy 

# class MyCustomTreeNode:
#     """Base Class that checks if the node is part of a Custom Node tree"""
#     @classmethod
#     def poll(cls, ntree):
#         return ntree.bl_idname == 'CustomNodeTreeType'

# class CustomNode(MyCustomTreeNode,bpy.types.Node):    
class CustomNode(bpy.types.Node):    
    """Base Node class from which to derive all further node classes"""
    bl_idname = 'CustomNodeType'
    bl_label = "Custom Node"

    @classmethod
    def poll(cls, ntree):
        return ntree.bl_idname == 'CustomNodeTreeType'

def register():
    bpy.utils.register_class(CustomNode)

def unregister():
    bpy.utils.unregister_class(CustomNode)