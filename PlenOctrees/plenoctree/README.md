# PlenOctrees: NeRF-SH training and conversion

This repository contains code to train a NeRF-SH model and to extract the PlenOctree. 

This code is created by [Alex Yu](https://github.com/sxyu) and [Ruilong Li](https://github.com/liruilong940607).

**Original Repository:** https://github.com/sxyu/plenoctree/tree/master

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

#### config/blender.yaml
- changed max_steps from 2,000,000 to 1,000,000

### config/real360.yaml
- created this using the tt.yaml as template.
- changed the number of iterations from 200 to 100,000
- changed the dataset to llff
- changed white_bkgd to false

#### nerf/model_utils.py
- TypeError: broadcast_to requires ndarray or scalar arguments, got <class 'list'> at position 0. -- change [1e10] to jnp.array(1e10) 
```
>>> # Original jnp.broadcast_to([1e10], z_vals[Ellipsis, :1].shape)
>>> jnp.broadcast_to(jnp.array(1e10), z_vals[Ellipsis, :1].shape) # edited
```

#### nerf/models.py
- import optax
- get_model_state(): use optax.adam instead of flax.optim.Adam and define the state using the newly defined TrainState

#### nerf/utils.py
- import optax and from typing import Any
- Change TrainState to use optax. Instead of having the following arguments: [optimizer, target, opt_state] it became [step, variables, optimizer, opt_state] since the optimizer opbject of optax does not store states the same way as flax.optim.
- Change rendering_every from 20,000 to 10,000 to see more statistics for exeperiments
- save checkpoints more often. save_every 10,000 to 5,000
- print more often from 1,000 to 500
- garbage collect more often. gc_every from 5,000 to 2,500
- change sparsity n_points from 10,000 to 5,000

#### train.py
- import optax and gpustat
- flax.checkpoints is depreciated. Adapting code to orbax for future-proofing: added the following at the start of the code 
```
>>> flax.config.update('flax_use_orbax_checkpointing', True)
``` 
- replaced arguments in train_step to be compatible to the new definition of the TrainState class
- change how to extract information from the state in loss_fn()
    - state.optimizer.target to state.variables
    - step has to be manually extracted using state.step
    - update learning rate separately by changing the hyperparameters in the opt_state in the saved state variable
    - replace three variables (step, variables, opt_state) in the state instead of jsut the optimizer.
- In main ():
    - add code to check and print the number of GPUs detected in the system
    - measure training time
    - host_id renamed to process_index() due to depreciation warnings
    - when opening txt files, change "a" to "a+" since there were times the error would show that the file is not in the directory
    - add gpu_stats together with print_every and save in FLAGS.train_dir+"/gpu_memory_consumption_training.txt"
    - to get eval_variables, changed from optimizer.target to variables
    - change strings to print to variables to be able to store them in text files easier.
    - save test evaluation in FLAGS.train_dir+"/summary_training.txt"
    - save total training time in FLAGS.train_dir+"/total_training_time_training.txt"

#### eval.py
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

#### evaluation.py
- import time
- add a default to write_vid instead of None. Use ./octrees/tree_render/rendered.mp4 so that by default it saves a video. This was used for checking experiments
- add a default write_images from None to ./octrees/tree_render so that it always saves images. This was also used for experiments.
- in main():
    - measure total training time and save in FLAGS.write_images+'/total_training_time_summary_octree_evaluation.txt'
    - print directory to save in for sanity check

#### extraction.py
- import time and gpustat
- change default projection samples from 10,000 to 5,000 based on experiments
- move up grid = grid.cuda()
- change mask to mask.cuda() in grid
- change refine_chunk from 2,000,000 to 1,000,000
- store timings in FLAGS.train_dir+"/total_training_time_extraction.txt"
- store GPU stats in FLAGS.train_dir+"/gpu_memory_consumption_extraction.txt"
- store psnr, ssim, lpips stats in FLAGS.train_dir+"/summary_extraction.txt"
- store total training time in FLAGS.train_dir+"/total_training_time_extraction.txt"

#### optimization.py
- import gpustat and time
- change default number of epochs to train for from 80 to 40
- measure and store total training time in FLAGS.train_dir+"/total_training_time_optimization.txt"
- save psnr per epoch in FLAGS.train_dir+"/summary_optimization.txt" 
- save GPU stats in FLAGS.train_dir+"/gpu_memory_consumption_optimization.txt"