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
