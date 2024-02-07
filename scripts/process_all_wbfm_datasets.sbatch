#!/usr/bin/env bash

#SBATCH --job-name=bundle_net
#SBATCH --nodes=1                   # Use one node
#SBATCH --ntasks=1                  # Run a single task
#SBATCH --qos=medium             # Time limit hrs:min:sec
#SBATCH --output=log_gpu_step-%j.out    # Standard output and error log
#SBATCH --time=8:00:00
#SBATCH --mem=16G
#SBATCH --cpus-per-task=16
#SBATCH --gpus-per-node=1
#SBATCH --partition=gpu
#SBATCH --gres=shard:32

pwd; hostname; date

# Could parallelize this, but it should be ~3 minutes per dataset (~2 hours total)
python process_all_wbfm_datasets.py
