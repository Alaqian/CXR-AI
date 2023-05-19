## Pipeline
### Install Dependencies
Directories:
- deps_dir = "root/deps/"
- repo_dir = "root/kohya-trainer"
- training_dir = "root/fine_tune/"
- pretrained_model = "root/pretrained_model/"
- vae_dir = "root/vae/"
- config_dir = "root/fine_tune/config/"

- accelerate_config = "root/kohya-trainer/accelerate_config/config.yaml"
- tools_dir = "root/kohya-trainer/tools"
- fine_tune_dir = "root/kohya-trainer/finetune"
- repo_url = "https://github.com/Linaqruf/kohya-trainer"
- bitsandytes_main_py = "/usr/local/lib/python3.10/dist-packages/bitsandbytes/cuda_setup/main.py"

1. cd into root directory
2. mkdir for dir in [deps_dir, training_dir, config_dir, pretrained_model, vae_dir]