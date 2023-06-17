bl_info = {
    "name": "Image Uniqueizer",
    "description": "Removes duplicate image nodes.",
    "author": "Jerome Stephan",
    "version": (0, 0, 0, 1),
    "blender": (2, 80, 0),
    "location": "File > Clean Up",
    "warning": "",
    "wiki_url": "https://secaproject.com/"
                "blender_addon_ascii",
    "tracker_url": "https://secaproject.com/blender_addon_ascii#report",
    "support": "OFFICIAL",
    "category": "Clean Up",
}


import bpy


def eliminate_node_groups(context, rename_first, self):
#    print("\nEliminate Node Group Duplicates:")

#    #--- Search for duplicates in the actual node groups
#    node_groups = bpy.data.node_groups

#    for group in node_groups:
#        for node in group.nodes:
#            if node.type == 'GROUP':
#                eliminate(node)

    #--- Search for duplicates in materials
    mats = list(bpy.data.materials)
    worlds = list(bpy.data.worlds)

    if rename_first:
        for mat in mats + worlds:
            if mat.use_nodes:
                for node in mat.node_tree.nodes:
                    if node.bl_idname == 'ShaderNodeTexImage':
                        rename_to_path(node)
    for mat in mats + worlds:
        if mat.use_nodes:
            for node in mat.node_tree.nodes:
                if node.bl_idname == 'ShaderNodeTexImage':
                    eliminate_images(node)

#--- Eliminate the node group duplicate with the original group if found
def eliminate(node):
    node_groups = bpy.data.node_groups

    # Get the node group name as 3-tuple (base, separator, extension)
    (base, sep, ext) = node.node_tree.name.rpartition('.')

    # Replace the numbered duplicate with original if found
    if ext.isnumeric():
        if base in node_groups:
            print("  Replace '%s' with '%s'" % (node.node_tree.name, base))
            node.node_tree.use_fake_user = False
            node.node_tree = node_groups.get(base)
            
def rename_to_path(node):
    if not hasattr(node.image, "filepath"):
        print("NO FILEPATH")
        return False
    (base, sep, ext) = node.image.filepath.rpartition('\\')
    if ext:
        print("  Replace name '%s' with '%s'" % (node.image.name, ext))
        node.image.name = ext
    return True
    
def eliminate_images(node):
    if not hasattr(node.image, "filepath"):
        print("NO FILEPATH")
        return False
    images = bpy.data.images
    
    (base, sep, ext) = node.image.name.rpartition('.')
    if ext.isnumeric():
        if base in images:
            print("  Replace node '%s' with '%s'" % (node.image.name, base))
            node.image.use_fake_user = False
            node.image = images.get(base)
    # print(images.get("//textures\damage-a-color.dds.001"))

class NodeUniqueizer(bpy.types.Operator):
    """Removes duplicate (image) nodes"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "uniqueize.nodes"        # Unique identifier for buttons and menu items to reference.
    bl_label = "Remove Dupes!"         # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.
    #--- Eliminate Node Group Duplicates
    rename_first: bpy.props.BoolProperty(name="Rename to Filepath?", default=False)
    
    def execute(self, context):
        eliminate_node_groups(context, self.rename_first, self)
        print("Node Uniquizer: All Done!")
        return {'FINISHED'}
    
    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

#--- Execute

def menu_func(self, context):
    self.layout.operator(NodeUniqueizer.bl_idname)

def register():
    bpy.utils.register_class(NodeUniqueizer)
    bpy.types.TOPBAR_MT_file_cleanup.append(menu_func)
    
def unregister():
    bpy.utils.unregister_class(NodeUniqueizer)
    bpy.types.TOPBAR_MT_file_cleanup.remove(menu_func)
    

if __name__ == "__main__":
    register()
