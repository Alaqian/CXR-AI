import os

MODEL = {
    "v1-4"
    "v1-5": {
        "name": "Stable-Diffusion-v1-5",
        "url": "https://huggingface.co/runwayml/stable-diffusion-v1-5/blob/main/v1-5-pruned.safetensors",
        "v2": False,
        "path": "pretrained_models/stable_diffusion_1_5-pruned.safetensors",
    },
    "v2": {
        "name": "stable-Diffusion-2",
        "url": "https://huggingface.co/stabilityai/stable-diffusion-2/resolve/main/768-v-ema.safetensors",
        "v2": True,
        "path": "pretrained_models/stable_diffusion_2-pruned.safetensors",
    }
    "v2-1": {
                
}