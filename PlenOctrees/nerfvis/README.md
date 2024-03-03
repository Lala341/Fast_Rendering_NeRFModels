Cloned from the following repository: https://github.com/sxyu/nerfvis/tree/master


# Nerfvis:

This repository contains the source code for the nerfvis library: In-browser 3D visualization library for rapid prototyping with built-in support for diffuse view-dependent sparse volumes (PlenOctrees).

This code is created by [Alex Yu](https://github.com/sxyu) with contributions by [Hang Gao](https://github.com/hangg7) .

**Original Documentation:** https://nerfvis.readthedocs.org
**Based on PlenOctrees** https://github.com/sxyu/plenoctrees

## Usage

Please see  [Rendering Jupyter Notebook](PlenOctrees/rendering.ipynb) for a guide on the usage of this module.

Since there are changes in the original index.html file, this repository must first be cloned. Then the module can be imported and used as:
```
>>> from nerfvis.nerfvis import scene # assuming you are executing this outside the cloned nerfvis repository
>>> scene.set_title(scene_title)
>>> scene.add_volume_from_npz(scene_label, file, scale=1.0)
>>> scene.display(port=port_number, open_browser=True) # or embed() to view in this same notebook.
```

## Changes

index.html
- adding a new div to the html body with id = statsDisplay which will contain additional rendering statistics
- adding FPS and loading time using: updateLoadTimeAndFPSDisplay(). This was added as javascript code in the html file, before the creating the Volrend variable.