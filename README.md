# Adapting Pretrained Stabled Diffusion model to generate Chest X-ray data

Final project for ECE-GY 6123
Members: Alaqian Zafar, Akshay Gowda and Chinmay Tompe

Abstract: We explore two different finetuning techniques to teach the model the concepts of a chest X-ray. We propose adopting a low-rank adaptation (LoRA) method with Dreambooth for fine- tuning large pre-trained language models, reducing the number of trainable parameters, for downstream tasks while maintaining model quality. Our approach can help generate synthetic chest X-rays and improve the availability of healthcare datasets. These images can potentially be used for training machine learning models, data augmentation, and clinical applications.
## Instructions
### Cloning Repository
Clone this repository using the following command:
```bash
git clone https://github.com/Alaqian/Chest-X-ray-Generator
```
Navigate to the cloned repository:
```bash
cd Chest-X-ray-Generator
```
Enter the following command to initialize and update all submodules:
```bash
git submodule update --init --recursive
```
### Installing Dependencies
Run the following command to install all dependencies:
```bash
python -m venv .venv
.venv\Scripts\activate
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
```
### Running the Code
#### Full fine-tuning
coming soon...
#### Low-rank adaptation (LoRA)
coming soon...

### Adding a Submodule
To add a submodule to this repository, first create a fork of the original repository.

Then you can use the git submodule add command followed by the URL of the forked repository. 
```bash
git submodule add https://github.com/example-username/example-repo.git
```
This will create a new directory in your repository that contains a clone of the "example-repo" repository.

Commit and push the changes to the main branch.
