import argparse
import json
import os

from huggingface_hub import hf_hub_download

PRETRAINED_MODELS = json.load(open("pretrained_models/pretrained_models.json"))
VAE = json.load(open("vae/vae.json"))


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
        "--vae",
        "-v",
        type=str,
        required=False,
        choices=list(VAE.keys()),
        help="VAE to download",
    )
    parser.add_argument(
        "--force_download",
        "-f",
        action="store_true",
        help="Force download model even if it exists",
    )
    return parser.parse_args()


def download_model(model, force=False, download_dir="pretrained_models"):
    filename = model["filename"]
    repo_id = model["repo_id"]
    if os.path.exists(f"{download_dir}/{filename}"):
        print(f"{repo_id} model already exists at {download_dir}/{filename}")
        if force:
            print(f"Overwriting {repo_id} model at {download_dir}/{filename}")
        else:
            return
    print(f"Downloading {repo_id}/{filename}")
    hf_hub_download(
        repo_id=repo_id,
        filename=filename,
        cache_dir=".cache",
        local_dir=download_dir,
        local_dir_use_symlinks=True
    )
    print(f"Downloaded {repo_id} at {download_dir}/{filename}")


if __name__ == "__main__":
    force = parse_args().force_download

    model_id = parse_args().model
    if model_id:
        model_info = PRETRAINED_MODELS[model_id]
        download_model(model_info, force)

    vae_id = parse_args().vae
    if vae_id:
        vae_info = VAE[vae_id]
        download_model(vae_info, force, download_dir="vae")
