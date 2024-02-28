# MobileNeRF Code Book

This code book accompanies the MobileNeRF repository, which contains the source code for the paper "MobileNeRF: Exploiting the Polygon Rasterization Pipeline for Efficient Neural Field Rendering on Mobile Architectures."

## Introduction

MobileNeRF is a project aimed at rendering neural fields efficiently on mobile architectures. Developed by Zhiqin Chen during his time as a student researcher at Google, this repository contains the implementation of the MobileNeRF algorithm. In addition to the original implementation, this code base includes updates to enhance compatibility with the latest versions of JAX and provides solutions to common errors encountered during execution.




## Data

Please download the datasets from the [NeRF official Google Drive](https://drive.google.com/drive/folders/128yBriW1IG_3NJ5Rp7APSTZsJqdJdfc1).
Please download and unzip `nerf_synthetic.zip` and `nerf_llff_data.zip`.

**(TODO: how to download unbounded scenes from Mip-NeRF 360?)**



## Installation 


### GPU compatible (Linux and Windows) with Optax


To set up the environment for running MobileNeRF, follow these steps:

1. Clone the repository to your local machine.
2. Use [Anaconda](https://www.anaconda.com/products/individual) to create a virtual environment with Python 3.10:
    ```
    conda create --name mobilenerf2 python=3.10
    conda activate mobilenerf2
    conda install pip; pip install --upgrade pip
    ```
3. Install the required dependencies by running:
    ```
    cd MobileNeRFGPU
    pip install -r requirements.txt
    ```

Note: The installation process assumes the availability of 8 V100 GPUs for successful training. Hoewer, you can comment the part of the code using this requirements, we execute this code using 2 V100 GPUs with good results.


### MacOs compatible (M1/M2)


To run MobileNeRF on macOS, you'll need to install `jax-metal` by following the instructions provided at [Apple Metal for JAX](https://developer.apple.com/metal/jax/). Ensure compatibility by referring to the information available on the official JAX documentation page: [JAX Installation Guide](https://jax.readthedocs.io/en/latest/installation.html#pip-installation-google-cloud-tpu).

After installing `jax-metal`, proceed with the instructions as follows.


To set up the environment for running MobileNeRF, follow these steps:

1. Clone the repository to your local machine.
2. Use [Anaconda](https://www.anaconda.com/products/individual) to create a virtual environment with Python 3.10:
    ```
    conda create --name mobilenerf2 python=3.10
    conda activate mobilenerf2
    conda install pip; pip install --upgrade pip
    ```
3. Install the required dependencies by running:
    ```
    cd MobileNeRFMac
    pip install -r requirements.txt
    ```


### Colab

For use in Google Colab, there is no need to install JAX separately as it is already included by default. However, please ensure that you install the necessary requirements found in the MobileNeRFColab folder. It's important to note that the code was tested using a TPU in Google Colab.


### Execution

The training code is in three .py files, corresponding to the three training stages: 1. continuous opacity, 2. binarization and supersampling, 3. extracting meshes and textures.

First, modify the parameters in all .py files:
```
scene_type = "synthetic"
object_name = "chair"
scene_dir = "datasets/nerf_synthetic/"+object_name

weights_dir = "results/"+ object_name+"/weights"
samples_dir = "results/"+object_name+"/samples"
metrics_dir = "results/"+object_name+"/metrics"

```
*scene_type* can be synthetic, forwardfacing, or real360. *object_name* is the name of the scene to be trained; the available names are listed in the code. *scene_dir* is the folder holding the training data.

if poses_bound are not provided in dataset. Follow the steps in ```https://github.com/Fyusion/LLFF``` to obtain poses.

Afterwards, run the three .py files consecutively
```
python stage1.py
python stage2.py
python stage3.py
```
The intermediate weights will be saved in folder *weights* and the intermediate outputs (sample testing images, loss curves) will be written to folder *samples*. The output meshes+textures will be saved in folder *obj_phone*.

Note: the stage-1 training could occasionally fail for unknown reasons (especially on the bicycle scene); switch to a different set of GPUs could solve this.

Note: For unbounded 360 degree scenes, ```stage3.py``` will only extract meshes of the center unit cube. To extract the entire scene, use ```python stage3_with_box.py```.

It takes 8 hours to train the first stage, 12-16 hours to train the second, and 1-3 hours to run the third.

## Running the viewer

The viewer code is provided in this repo, as three .html files for three types of scenes.

You can set up a local server on your machine, e.g.,
```
cd folder_containing_the_html
python -m http.server
```
Then open
```
localhost:8000/view_synthetic.html?obj=chair
```
Note that you should put the meshes+textures of the chair model in a folder *chair_phone*. The folder should be in the same directory as the html file.

Please allow some time for the scenes to load. Use left mouse button to rotate, right mouse button to pan (especially for forward-facing scenes), and scroll wheel to zoom. On phones, Use you fingers to rotate or pan or zoom. Resize the window (or landscape<->portrait your phone) to show the resolution.


# Contributions

One of the significant contributions of this repository is the transition from using the `optim` module to adopting `optax` as the optimizer. This change was made to ensure compatibility with the latest version of JAX, as the `optim` module has been disabled in recent releases. By leveraging `optax`, the codebase benefits from updated optimization algorithms and improvements in efficiency. For more information on how to replace `optim` with `optax`, you can refer to the Flax documentation's [Optax Update Guide](https://flax.readthedocs.io/en/latest/guides/converting_and_upgrading/optax_update_guide.html). Additionally, details about the `optax.adam` optimizer can be found in the Optax documentation's [Adam API reference](https://optax.readthedocs.io/en/latest/api.html#optax.adam).



## Common errors

## Compatibility with Latest Versions of JAX

Please be aware of compatibility issues with the latest versions of JAX. If you encounter an error similar to the following:


AttributeError: module 'flax' has no attribute 'optim'


This error occurs because the latest versions of JAX have disabled the `optim` module. Therefore, one of the key contributions of this project is the transition from using the `optim` module to utilizing `optax`. To ensure compatibility, make sure you are using the latest version of JAX. You can find compatibility information and installation instructions for JAX on the official documentation page: [JAX Installation Guide](https://jax.readthedocs.io/en/latest/installation.html#pip-installation-google-cloud-tpu)



### Compatibility errors JAX

If you encounter issues with device compatibility or installing GPU-compatible JAX, it's crucial to find the correct version. You can check compatibility information and find the appropriate installation instructions on the official JAX documentation page: [JAX Installation Guide](https://jax.readthedocs.io/en/latest/installation.html#pip-installation-google-cloud-tpu)




