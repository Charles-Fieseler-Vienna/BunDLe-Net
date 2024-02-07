#!/usr/bin/env bash

#SBATCH --job-name bundle_net
#SBATCH --partition=gpu
#SBATCH --gres=shard:32
#SBATCH --cpus-per-task=8
#SBATCH --mem=20G
#SBATCH --time=0-12:00:00

pwd; hostname; date

# Could parallelize this, but it should be ~3 minutes per dataset (~2 hours total)
python process_all_wbfm_datasets.py
