# Loop through folders and apply the bundle net process to all datasets
from pathlib import Path
from tqdm import tqdm

from bundle_net.functions import full_pipeline


data_base_dir = "/scratch/neurobiology/zimmer/fieseler/multiproject_visualizations"

subfolders = ['bundle_net', 'bundle_net_gfp', 'bundle_net_immob']

for subfolder in tqdm(subfolders):
    parent_dir = Path(data_base_dir) / subfolder
    for data_dir in tqdm(Path(parent_dir).iterdir(), leave=False):
        full_pipeline(data_dir)
