import argparse
import json
import os

from tqdm import tqdm
from huggingface_hub import hf_hub_download

PRETRAINED_MODELS = json.load(open("pretrained_models/pretrained_models.json"))
# VAE = json.load(open("vae/vae.json"))


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--model",
        "-m",
        type=str,
        required=False,
        choices=list(PRETRAINED_MODELS.keys()),
        help="Model to download",
    )
    parser.add_argument(
        "--force_download",
        "-f",
        action="store_true",
        help="Force download model even if it exists",
    )
    return parser.parse_args()


def download_model(model, force=False):
    filename = model["filename"]
    repo_id = model["repo_id"]
    if os.path.exists(f"pretrained_models/{filename}"):
        print(f"{repo_id} model already exists at pretrained_models/{filename}")
        if force:
            print(f"Overwriting {repo_id} model at pretrained_models/{filename}")
        else:
            return
    print(f"Downloading {repo_id}/{filename}")
    hf_hub_download(repo_id=repo_id, filename=filename, local_dir=f"pretrained_models",local_dir_use_symlinks=False)
    print(f"Downloaded {repo_id} at pretrained_models/{filename}")


if __name__ == "__main__":
    model_id = parse_args().model
    force = parse_args().force_download
    if model_id:
        model_info = PRETRAINED_MODELS[model_id]
        download_model(model_info, force)
