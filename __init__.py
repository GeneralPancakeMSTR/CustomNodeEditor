import bpy 
# https://github.com/blender/blender/blob/main/scripts/templates_py/custom_nodes.py
# https://github.com/atticus-lv/simple_node_tree/blob/master/__init__.py

bl_info = {
    "name":"Custom Node Tree",
    "author": "PancakeMSTR",
    "version":(0,0),
    "blender":(3,6,0),
    "location": "Node Editor > Simple Editor",
    "description": "Custom Node Tree Example",
    "category": "Node"
}



# root_modules ("sverchok")
root_modules = [
    "dependencies",
    "data_structure",
    "node_tree",
    "core",  # already imported but should be added to use register function
    "utils",  # already imported but should be added to use register function
    "ui",
    "nodes",
    "old_nodes"
]

# core_modules ("sverchok.core")
core_modules = [
    "sv_custom_exceptions",
    "update_system",
    "sockets",
    "socket_data",
    "handlers",
    "events",
    "node_group",
    "tasks",
    "group_update_system",
    "event_system"
]

# ui.module_names() ("sverchok.ui")
ui_module_names = [
    "add_nodes_panel",
    "bgl_callback_3dview",
    "bgl_callback_nodeview",
    "color_def",
    "development",
    "nodes_replacement",
    "nodeview_operators",
    "nodeview_rclick_menu",
    "nodeview_space_menu",
    "presets",
    "profile_panel",
    "sv_3d_panel",
    "sv_examples_menu",
    "sv_extra_addons",
    "sv_extra_search",
    "sv_icons",
    "sv_image",
    "sv_IO_panel",
    "sv_panel_display_nodes",
    "sv_panels",
    "sv_temporal_viewers",
    "sv_vep_connector",
    "testing_panel",
    "text_editor_plugins",
    "text_editor_submenu",
    "utils",
    "zoom_to_node",
    "nodeview_keymaps" # puts this one at the end 
]

# def import_settings(imported_modules):
#     """Useful have the function to be sure that we do not import half of
#     Sverchok modules wia settings"""
#     settings = importlib.import_module(".settings", "sverchok")
#     imported_modules.append(settings)

import importlib
import os
import sys 
import traceback


os.system('cls')

# mods_bases = [
#     ([module_00,module_01,...],"base_0"),
#     ([module_10,module_11,...],"base_1"),
#     ...
# ]

# List of imported module objects 
# imported_modules = [
#     importlib.import_module(".settings","sverchok"), # <- import_settings(imported_modules), imports sverchok.settings
#     importlib.import_module(".sv_logging","sverchok.utils"), # <- import_logging(imported_modules), imports sverchok.utils.sv_logging
#     importlib.import_module(".module_00","base_0"), # <- import_all_modules(imported_modules,mods_bases); imports base_0.module_00
#     importlib.import_module(".module_01","base_0"), # imports base_0.module_01
#     importlib.import_module(".module_10","base_1"), # imports base_1.module_10
#     importlib.import_module(".module_11","base_1"), # imports base_1.module_11    
#     ...
# ]


modules = [
    # core (/)
    importlib.import_module("custom_node_editor.editor"),
    importlib.import_module("custom_node_editor.node"),
    # ui (/ui)
    importlib.import_module("custom_node_editor.ui.editor_add_menu")
]

def register():
    # core = sverchok/core/__init__.py
    # core.sv_register_modules(imported_modules) -> For each imported module, call module_object.register() (if object has register() method)
    # -> register util modules: One of the root modules is sverchok.utils : register function explicitly registers these. I don't know why. 
    # -> register node_modules 
    # node_modules is acquired from the core.import_nodes() call. 
    #   This call basically goes through all of the folders in nodes and imports things based on the directory structure, 
    #   ignoring __pycache__ directories and __init__.py files. 

    try:
        for module in modules:
            module.unregister()
    except RuntimeError:
        # Modules have not been registered         
        # print(traceback.format_exc())
        pass 

    for module in modules:
        importlib.reload(module)
        module.register()

def unregister():    
    for module in modules:
        module.unregister()

if __name__ == '__main__':
    register()