# PlenOctrees: NeRF-SH training and conversion

This repository contains code to train a NeRF-SH model and to extract the PlenOctree. 

This code is created by [Alex Yu](https://github.com/sxyu) and [Ruilong Li](https://github.com/liruilong940607).

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

Clone this repository and install the requirements.
```
pip install -r requirements.txt
```

For additional set up information, especially for Google Colab (T4 GPU or V100), please see [NeRF-SH Training and Conversion](PlenOctrees/nerfsh-train-convert-colab-compatible.ipynb).

Another notebook is available for the implementation for a pretrained JaxNeRF model in this notebook [JaxNeRF to Octrees](PlenOctrees/pretrained-jaxnerf-colab-compatible.ipynb)

Note that for the Google colab implementation, there is no need to change the pre-installed Jax, CUDA, and Flax. 

## Examples

Our trained NeRF-SH models and plenoctrees can be found at [Google Drive]()

## Changes

Note that all changes can be found by looking up "#!" in the code.

### Requirements
- added tqdm, gpustat for additional permonance metrics
- added optax to replace flax.optim

### NeRF-SH Training

nerf/utils.py

train.py
- import optax and gpustat
- flax.checkpoints is depreciated. Adapting code to orbax for future-proofing: added the following at the start of the code 
```
>>> flax.config.update('flax_use_orbax_checkpointing', True)
``` 
- replaced arguments in train_step to be compatible to the new definition of the TrainState

eval.py
- flax.checkpoints is depreciated. Adapting code to orbax for future-proofing: added the following at the start of the code 
```
>>> flax.config.update('flax_use_orbax_checkpointing', True)
``` 
- changed step from state.optimizer.state.step to state.step
- changes state.optimizer.target to state.variables
- uncommented the section to print statistics on PSNR and SSIM 
- saves statistics to a text file FLAGS.train_dir+"/summary_training_eval.txt"
- host_id renamed to process_index() due to depreciation warnings

### PlenOctree Conversion
- 
