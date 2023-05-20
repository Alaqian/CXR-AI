import argparse
import json
import os

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
    return parser.parse_args()


if __name__ == "__main__":
    model = parse_args().model
    
