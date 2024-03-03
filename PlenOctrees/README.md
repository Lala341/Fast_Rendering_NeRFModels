# PlenOctrees

This repository contains code to train a NeRF-SH model, extract the PlenOctree, and render it. Please see individual directories for more information.

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

## Notes
All codes are based on the works of previous authors as cited in the respective directories.

Jupyter notebooks are availeble that are compatible with Google Colab for both NeRF-SH training and JaxNeRF octree extraction. The rendering notebook can also be used on Google Colab but a tunnel must be established to allow the simulation of a localhost connection. Alternatively, the scene can also be viewed within the jupyter notebook itself.