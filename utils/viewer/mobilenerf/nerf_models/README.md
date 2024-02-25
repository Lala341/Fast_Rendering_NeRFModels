# MobileNeRF


This code is created by [Zhiqin Chen](https://czq142857.github.io/) when he was a student researcher at Google.

*Please note that this is not an officially supported Google product.*


## Running the viewer

The viewer code is provided in this repo, as three .html files for three types of scenes.

You can set up a local server on your machine, e.g.,
```
python -m http.server
```
Then open
```
localhost:8000
```
Note that you should put the meshes+textures of the chair model in a folder *chair_phone*. The folder should be in the same directory as the html file.

Please allow some time for the scenes to load. Use left mouse button to rotate, right mouse button to pan (especially for forward-facing scenes), and scroll wheel to zoom. On phones, Use you fingers to rotate or pan or zoom. Resize the window (or landscape<->portrait your phone) to show the resolution.