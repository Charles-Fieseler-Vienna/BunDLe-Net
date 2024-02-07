# Loop through folders and apply the bundle net process to all datasets
from pathlib import Path
from tqdm import tqdm
import argparse

from bundle_net.functions import full_pipeline


def main(DEBUG=False):
    data_base_dir = "/scratch/neurobiology/zimmer/fieseler/multiproject_visualizations"

    subfolders = ['bundle_net', 'bundle_net_gfp', 'bundle_net_immob']

    for subfolder in tqdm(subfolders):
        parent_dir = Path(data_base_dir) / subfolder
        for data_dir in tqdm(Path(parent_dir).iterdir(), leave=False):
            full_pipeline(data_dir)
            if DEBUG:
                break
        if DEBUG:
            break
    print("Finished processing all datasets")


if __name__ == "__main__":
    # One flag: run_all or not
    parser = argparse.ArgumentParser(description='Build interactive gridplot')
    parser.add_argument('--DEBUG', default=False, help='')
    args = parser.parse_args()

    DEBUG = True if args.DEBUG == "True" else False

    main(DEBUG=DEBUG)
