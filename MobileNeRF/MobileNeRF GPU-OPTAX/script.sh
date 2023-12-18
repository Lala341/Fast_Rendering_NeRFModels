#!/bin/bash
#SBATCH --nodes=1
#SBATCH --time=10:00:00
#SBATCH -p gpua100
#SBATCH --gres=gpu:2
#SBATCH --mem=50G
#SBATCH --export=none
#SBATCH --job-name=hub1
#SBATCH --output=outputJob.txt



# Your commands to run on the cluster go below this line
echo "Hello, this is my Slurm job!"


module load miniconda3/23.5.2/gcc-13.2.0


# Run your Python script
python stage83.py



 