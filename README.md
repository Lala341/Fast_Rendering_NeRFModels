# Fast_Rendering_Plenoctrees

Names: 

- Adina Faye Bondoc
- Laura Isabella  Forero Camacho
- Chidiebere Ogbuchi


## Objetive


3D reconstruction using Neural Radiance Fields (NeRF) is computationally demanding, making it impractical for real-time applications. The MobileNeRF and PlenOctree models offer promising solutions, enabling real-time rendering. This project seeks to replicate and evaluate these models to gauge their effectiveness in rendering NeRF models within a web browser using custom data.

## Exploration and Result Models for Step 1
In our project, we have embarked on a journey of exploration and experimentation, particularly focusing on the initial phase, known as "Step 2." This phase involves diving into the world of 3D reconstruction using Neural Radiance Fields (NeRF) and harnessing the power of the MobileNeRF PlenOctree for real-time rendering. To facilitate this exploration, we have organized our directory structure as follows:


### Repository

# Repository Description

This repository is dedicated to the exploration and enhancement of 3D reconstruction using Neural Radiance Fields (NeRF). The conventional NeRF models face computational challenges, rendering them impractical for real-time applications. In response, this project focuses on the implementation and evaluation of two promising models, MobileNeRF and PlenOctree, which offer solutions for achieving real-time rendering.

## Folder Structure Overview

### `utils`
- `metrics`: Utility functions for evaluating model metrics.
- `viewer`: Components related to the web-based viewer.
  - `nerf_synthetic`: Synthetic data for NeRF model evaluation.
    - Specific scenes such as `ficus_phone`, `drumsBDRP2_phone`, `ship_phone`, etc.

### `SmallNeRFs`
- `EDP_NeRF`: Implementation of a Small NeRF variant.
- `Tiny_NeRF`: Implementation of another Small NeRF variant.

### `PlenOctrees`
- `nerfvis`: PlenOctree visualization using Python. Based on the python library of the same name
- `plenoctree`: PlenOctree implementation: NeRF-SH training and Octree building.
  - `nerf_sh`: Training and evaluation of the NeRF-SH model.
  - `octree`: Creation of the plenoctree from a NeRF model (NeRF-SH or JaxNeRF).
- `volrend`: PlenOctree visualization using a C++ application (local and web available).

### `MobileNeRF`
- `datasets`: Datasets for model training and evaluation.
  - `nerf_synthetic`: Synthetic data for NeRF model training.
    - Specific scenes such as `chair`, `drums`, etc.
- `results`: Model training results and associated data.
  - Specific subdirectories for different scenes (`drumsStage2`, `drums`, `chair`, etc.).
    - Subdirectories further organized by metrics, object files, weights, and samples.
### `MobileNeRF M2-Mac` 
- MobileNeRF implementation optimized for M2-based MacBook Pro.

### `MobileNeRF TPU-Colab-OPTAX`
- MobileNeRF implementation optimized for TPU (Notebooks).
- `datasets`: Datasets specific to TPU-Colab-OPTAX setup.
  - Subdirectories for weights, chair dataset, and samples.

### `MobileNeRF GPU-OPTAX`
- Implementation of MobileNeRF optimized for GPU with the OPTAX optimizer.

This organized folder structure facilitates the replication, evaluation, and improvement of MobileNeRF and PlenOctree models, with a specific focus on rendering NeRF models within a web browser using custom data. 



## References

**NeRF Original Paper**
- **Title**: [NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis](Paper_Link)
- **Authors**: Ben Mildenhall, Pratul P. Srinivasan, Matthew Tancik, Jonathan T. Barron, Ravi Ramamoorthi, Ren Ng
- **Published in**: ECCV 2020
- **Link**: [Read the paper](https://dl.acm.org/doi/pdf/10.1145/3503250)

**NeRF on Device**
- **Authors**: Jennifer(Kaiqi) Wu and Venkat S. Rao
- **Published on**: Stanford University CS231A (Previous Projects 2022)
- **Link**: [Access the document](https://web.stanford.edu/class/cs231a/prev_projects_2022/final_project__2_.pdf)

**PlenOctrees for Real-time Rendering of Neural Radiance Fields**
- **Authors**: Alex Yu, Deqing Sun, Forrester Cole, Jitendra Malik
- **Published on**: arXiv, 2021
- **Link**: [Read the paper](https://arxiv.org/pdf/2103.14024.pdf)

**MobileNeRF: Exploiting the Polygon Rasterization Pipeline for Efficient Neural Field Rendering on Mobile Architectures**
- **Authors**: Zhiqin Chen, Thomas Funkhouser, Peter Hedman, Andrea Tagliasacchi
- **Published on**: The Conference on Computer Vision and Pattern Recognition (CVPR), 2023
- **Citation**: Chen, Z., Funkhouser, T., Hedman, P., & Tagliasacchi, A. (2023). MobileNeRF: Exploiting the Polygon Rasterization Pipeline for Efficient Neural Field Rendering on Mobile Architectures. In *The Conference on Computer Vision and Pattern Recognition (CVPR)*.
- **Link to the Paper**: [Read the paper](https://arxiv.org/pdf/2103.14024.pdf)
