import argparse
import json
import os

from tqdm import tqdm
from transformers import AutoModelForSeq2SeqLM
from transformers import AutoTokenizer

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
    path = model["path"]
    url = model["url"]
    name = model["name"]
    if os.path.exists(path):
        print(f"{name} already exists at {path}")
        if force:
            print(f"Overwriting {name} at {path}")
        else:
            return
    print(f"Downloading {name}")
    with tqdm(
        unit="B", unit_scale=True, unit_divisor=1024, miniters=1, desc=name
    ) as progress_bar:
        print("Download complete!")


if __name__ == "__main__":
    model_id = parse_args().model
    force = parse_args().force_download
    if model_id:
        model = PRETRAINED_MODELS[model_id]
        download_model(model, force)
