import bpy 

custom_tree_types = {'CustomNodeTreeType'}

# c.f.  SverchokContext
class CustomNodesContext:
    """Checks if the current node tree is part of the Custom Editor (context)"""
    @classmethod
    def poll(cls, context):        
        tree_type = getattr(context.space_data, 'tree_type', None)
        if tree_type in {'CustomNodeTreeType'}:
            return True 

        # return context.space_data.tree_type == 

# def setup_add_menu():
#     # Stuff 
#     # global add_node_menu 
#     # add_node_menu = Category.from_config(yaml file as dict?, <name>,<icon>)
#     pass 

# class CategoryMenuTemplate(CustomNodesContext):
#     bl_label = ''

#     def draw(self,context): 
#         if not getattr(context.space_data,'edit_tree',None):
#             self.layout.operator("node.new_node_tree",text="New Custom Nodes Tree")
#             return 

# class Category():
#     def __init__(self,name,menu_cls,icon_name='BLANK1',extra_menu=''):
#         self.name = name
#         self.icon = icon_name 
#         self.extra_menu = extra_menu 
#         self.menu_cls = menu_cls 

#     def draw(self,layout):
#         layout.menu(self.menu_cls.__name__)

#     # def register(self):
#         # bpy.utils.register_class()

#     @classmethod 
#     def from_function(self):
#         # The way they are using type here is actually defining 
#         # a new class and creating an instance of it. 
#         cls_name = 'NODEVIEW_MT_CustomNodesCategory_Test'
#         base_classes = (CategoryMenuTemplate,bpy.types.Menu)
#         attributes = {'bl_label': 'menu_name'}
#         menu_cls = type(cls_name,base_classes,attributes)
#         print(menu_cls)
#         print(dir(menu_cls))
#         return menu_cls

class NODEVIEW_MT_CustomAddMenu(bpy.types.Menu):    
    """A custom add menu for this custom node editor """
    
    ######## Required ########
    # Shared and common to all classes 
    bl_label = 'Custom Add Menu' 

    def draw(self,context): 
        if not getattr(context.space_data,'edit_tree',None):
            self.layout.operator("node.new_node_tree",text="New Custom Nodes Tree")
            return 
        else:            
            properties = self.layout.operator("node.add_node",text='Add Custom Node (A)')            
            properties.type = 'CustomNodeType'

    @classmethod
    def poll(cls, context):        
        tree_type = getattr(context.space_data, 'tree_type', None)
        if tree_type in {'CustomNodeTreeType'}:
            return True 


# c.f. def sv_draw_menu(self,context)
def draw_custom_add_menu(add_menu,context):
    """Entry function to draw the Custom Nodes Add Menu"""
    if not context.space_data.tree_type in custom_tree_types:
        return 

    add_menu.layout.menu_contents('NODEVIEW_MT_CustomAddMenu')

def register():
    bpy.types.NODE_MT_add.append(draw_custom_add_menu)

    bpy.utils.register_class(NODEVIEW_MT_CustomAddMenu)

def unregister():
    bpy.types.NODE_MT_add.remove(draw_custom_add_menu)

    bpy.utils.unregister_class(NODEVIEW_MT_CustomAddMenu)

    
    


