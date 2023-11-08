# Fast_Rendering_Plenoctrees

Names: 

- Adina Faye Bondoc
- Laura Isabella  Forero Camacho
- Chidiebere Ogbuchi


## Objetive


3D reconstruction using Neural Radiance Fields (NeRF) is computationally intensive, making it unsuitable for real-time applicaBons. The plenOctree offers a promising soluBon by enabling real-time rendering. This project aims to replicate plenOctree and test its capabilities to render NeRF models in a web browser for custom data.

## Exploration and Result Models for Step 1
In our project, we have embarked on a journey of exploration and experimentation, particularly focusing on the initial phase, known as "Step 1." This phase involves diving into the world of 3D reconstruction using Neural Radiance Fields (NeRF) and harnessing the power of the PlenOctree for real-time rendering. To facilitate this exploration, we have organized our directory structure as follows:


### Folder Structure

**NeRF**

**EDP_NeRF**

In the ./NeRF/EDP_NeRF directory, we delve into the Extended Data Preparation (EDP) for NeRF. Here, we have the Edp_nerf_run.ipynb notebook, which serves as our virtual laboratory. Within this notebook, we experiment with different data preparation techniques, pushing the boundaries of data processing to enhance the capabilities of our NeRF models.

**Tiny_NeRF**

The ./NeRF/Tiny_NeRF directory is our playground for working with smaller-scale NeRF models, often referred to as "Tiny NeRFs." In this realm, we are experimenting with a range of techniques to fine-tune these miniature models for specific use cases.

BDRP_tiny_nerf_with_Visualization.ipynb takes us on a journey to understand how these tiny NeRFs can be used with various visualization techniques, allowing us to gain insights into the generated data.

BDRP_tiny_nerf_pytorch.ipynb introduces us to the PyTorch framework for training and enhancing our tiny NeRF models.
tiny_nerf.ipynb is where we continue to experiment with these compact NeRFs, pushing the boundaries of what they can achieve.

tiny_nerf_data.npz houses the data used for training and testing these models, serving as the foundation for our exploratory work.

**Plenoctrees**

The real-time rendering capabilities of the PlenOctree hold significant promise for our project. In the ./Plenoctrees directory, we explore its various implementations.

**nerf_sh**
In the ./Plenoctrees/nerf_sh subdirectory, we encounter one of the exciting NeRF variants. This specialized version introduces the use of spherical harmonics for representing radiance fields, promising to enhance the quality of our 3D reconstructions.

**octree**
The ./Plenoctrees/octree subdirectory is where we explore the inner workings of the PlenOctree, focusing on its octree data structure, pipeline optimizations, and real-time rendering capabilities. This exploration is pivotal to our mission of achieving real-time NeRF rendering in web browsers.

Our directory structure not only organizes our exploration but also forms the foundation for the development of new tools and methodologies to advance our project. As we progress through these directories, we aim to harness the power of NeRF and PlenOctrees, pushing the boundaries of what can be achieved in 3D reconstruction and rendering.

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

**Matthew Tancik's NeRF Project Website**
- **Author**: Matthew Tancik
- **Link**: [Visit the website](https://www.matthewtancik.com/nerf)

**PlenOctrees For Real-time Rendering of Neural Radiance Fields**
- **Authors**: Alex Yu, Deqing Sun, Forrester Cole, Jitendra Malik
- **Published at**: ICCV 2021 (Oral)
- **Link**: [Official website](https://alexyu.net/plenoctrees/)
