# Volrend: PlenOctree Volume Rendering

This is repository contains a real-time PlenOctree volume renderer using C++ and OpenGL

This code is created by [Alex Yu](https://github.com/sxyu) with contributions from [Ignacio Rocco](https://github.com/ignacio-rocco).

**Original Repository:** https://github.com/sxyu/volrend

**Based on PlenOctrees** https://github.com/sxyu/plenoctrees

PlenOctrees for Real Time Rendering of Neural Radiance Fields<br>
Alex Yu, Ruilong Li, Matthew Tancik, Hao Li, Ren Ng, Angjoo Kanazawa

https://alexyu.net/plenoctrees

```
@inproceedings{yu2021plenoctrees,
      title={{PlenOctrees} for Real-time Rendering of Neural Radiance Fields},
      author={Alex Yu and Ruilong Li and Matthew Tancik and Hao Li and Ren Ng and Angjoo Kanazawa},
      year={2021},
      booktitle={ICCV},
}
```

## Setup

Clone this repository and build the C++ project the same way the original authors had intended for WEB RENDERING. Please see (Volrend Github)[https://github.com/sxyu/volrend]

## Changes

Note that all changes can be found by looking up "#!" in the code.

### web/index.html
- move fps counter to the top right corner
- add additional list elements for Used JS heap metric and loading time
- add overall reset button

### web/js/emModule.js
- Update loading time and used heap in cppReportProgress()

### web/js/guiComponents.js
- Add overall reset button function for view direction shifting, sh decompose, slicing, backlight, octree grid

### web/js/init.js
- add startTime initialization