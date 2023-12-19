#  Copyright 2021 The PlenOctree Authors.
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are met:
#
#  1. Redistributions of source code must retain the above copyright notice,
#  this list of conditions and the following disclaimer.
#
#  2. Redistributions in binary form must reproduce the above copyright notice,
#  this list of conditions and the following disclaimer in the documentation
#  and/or other materials provided with the distribution.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
#  ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
#  LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
#  CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
#  SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
#  INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
#  CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
#  ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
#  POSSIBILITY OF SUCH DAMAGE.
"""Evluate a plenoctree on test set.

Usage:

export DATA_ROOT=./data/NeRF/nerf_synthetic/
export CKPT_ROOT=./data/PlenOctree/checkpoints/syn_sh16
export SCENE=chair
export CONFIG_FILE=nerf_sh/config/blender

python -m octree.evaluation \
    --input $CKPT_ROOT/$SCENE/octrees/tree_opt.npz \
    --config $CONFIG_FILE \
    --data_dir $DATA_ROOT/$SCENE/
"""
import torch
import numpy as np
import os
from absl import app
from absl import flags
from tqdm import tqdm
import imageio

from octree.nerf import models
from octree.nerf import utils
from octree.nerf import datasets

import svox
import time #! add time

FLAGS = flags.FLAGS

utils.define_flags()

flags.DEFINE_string(
    "input",
    "./tree_opt.npz",
    "Input octree npz from optimization.py",
)
flags.DEFINE_string(
    "write_vid",
    "/content/drive/.shortcut-targets-by-id/1PDxEvA_jKpTEuYgZl8WJItUoMS1hkgbM/bdrp/plenoctree/data/pretrained/jaxnerf/chair/octrees/tree_render/rendered.mp4", #! Change from None
    "If specified, writes rendered video to given path (*.mp4)",
)
flags.DEFINE_string(
    "write_images",
    "/content/drive/.shortcut-targets-by-id/1PDxEvA_jKpTEuYgZl8WJItUoMS1hkgbM/bdrp/plenoctree/data/pretrained/jaxnerf/chair/octrees/tree_render", #! change this to save images from None
    "If specified, writes images to given path (*.png)",
)

device = "cuda" if torch.cuda.is_available() else "cpu"

@torch.no_grad()
def main(unused_argv):
    
    total_training_start= time.time()#! Time taken for the entire process
    utils.set_random_seed(20200823)
    utils.update_flags(FLAGS)

    print('Saving in:', FLAGS.write_images) #! add for sanity check
    dataset = datasets.get_dataset("test", FLAGS)

    print('N3Tree load', FLAGS.input)
    t = svox.N3Tree.load(FLAGS.input, map_location=device)

    avg_psnr, avg_ssim, avg_lpips, out_frames = utils.eval_octree(t, dataset, FLAGS,
            want_lpips=True,
            want_frames=FLAGS.write_vid is not None or FLAGS.write_images is not None)
    print('Average PSNR', avg_psnr, 'SSIM', avg_ssim, 'LPIPS', avg_lpips)
    
    #! Save total optimization time
    with open(FLAGS.write_images+"/total_training_time_summary_octree_evaluation.txt", "a") as f:
        f.writelines(f"Total Extraction Time: {time.time()-total_training_start} seconds\n")
        f.writelines(f"avg_psnr={avg_psnr}, avg_ssim={avg_ssim}, avg_lpips={avg_lpips}\n")
    #!

    if FLAGS.write_vid is not None and len(out_frames):
        print('Writing to', FLAGS.write_vid)
        imageio.mimwrite(FLAGS.write_vid, out_frames)


    if FLAGS.write_images is not None and len(out_frames):
        print('Writing to', FLAGS.write_images)
        os.makedirs(FLAGS.write_images, exist_ok=True)
        for idx, frame in tqdm(enumerate(out_frames)):
            imageio.imwrite(os.path.join(FLAGS.write_images, f"{idx:03d}.png"), frame)

if __name__ == "__main__":
    app.run(main)
