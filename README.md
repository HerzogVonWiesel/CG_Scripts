# CG_Scripts
A collection of scripts I have written for CG-related work

## Scripts
### `_RG_NORMALS.py`

#### Description

This script converts a set of `green` (2 channel) normal maps, as often used in games, as PNG images into `blue` (3 channel) normal maps. It calculates the blue channel using the provided formula: `blue_channel = sqrt(1 - clamp(red_channel^2 + green_channel^2))`.

#### Prerequisites
- Python 3.x
- Python Imaging Library (PIL) package (pip install Pillow)

#### Usage
- Place the script in the same directory where your PNG images are located.
- Run the script.
- The script will create a new folder called `output` and place the converted normal maps in there.

---
---

## Blender Addons / Scripts

### `Remove_Duplicate_Nodes.py`

#### Description

This script removes duplicate image nodes from the node tree of all materials. It does this by comparing the names of the nodes and removing the duplicates.

#### Prerequisites
- Blender 2.8x

#### Usage
- Put the script in the `scripts/addons` folder of your Blender installation.
- Enable the addon in the preferences.
- It can then be found under `File > Clean Up > Node Uniqueizer`.

---

### `secascii_tlou2.py`

#### Description

This script is quite specific to the unpacked game files of The Last Of Us 2. It reads in the `.ascii` files spit out by the map extractor created by daemon1. I modified it such that it doesn't create a material for each mesh / submesh (which can result in thousands of duplicated materials and image nodes), but creates a single file for each shader, for which it reads in all texture files referenced in the `.ascii`.

#### Prerequisites
- Blender 2.8x

#### Usage
- Put the script in the `scripts/addons` folder of your Blender installation.
- Enable the addon in the preferences.
- It can then be found under `File > Import > ASCII (.ascii)`.