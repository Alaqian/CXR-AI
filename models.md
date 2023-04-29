# Models and Training Options
## 1. Stanford (Original Chest X-ray Model)
Experiments were conducted on 64 A100 GPUs split across two compute instances. Models were mostly trained (unless otherwise specified) in bf16 precision, as this led to 1/3 reduction of training time. Using bf16 precision, no significant training time difference was noticed across the various experiments, whether they fine-tuned one or several SD components, except when changing the number of training steps itself. At an image resolution of 512x512 px, an A100 GPU fine-tuning SD can hold a batch size of 8 (bf16 precision). Splitting batches across the GPUs of each compute instance, models were trained with a batch size of 256. In this setting, fine-tuning a model for 1k training steps took approximately 20 minutes; for 12.5k training steps, around 5 hours; for 60k training steps, one day.

Model weights for the SD pipeline (version 1.4) were obtained from the repository ”CompVis/stable-diffusionv1-4”(Hugging Face hub [53]), unless otherwise specified.

The code implementation was built on both the diffusers library [50] and the ViLMedic library [8]. Two domainspecific text encoders were used: RadBERT [4], downloadable on the HuggingFace repo StanfordAIMI/RadBERT, and SapBERT [20] available at cambridgeltl/SapBERTfrom-PubMedBERT-fulltext. In the experiments that follow, guidance scale 4 and 75 inference steps with a PNDM noise scheduler [21] enabled the generation of synthetic images properly conditioned on the associated prompts.
### Dataset
1. CheXpert Dataset
2. MIMIC-CXR Dataset

From each dataset, 1000 frontal (i.e., anterior-posterior or posterior-anterior projection) radiographs were sampled randomly for this study. 

Five images with no apparent findings, and five images featuring clearly visible pleural effusion as sole finding were manually selected. Unusually cropped or colorized images were discarded. The selected images were paired with a set of simple, synthetically generated prompts to form image-text pairs used for fine-tuning the Stable Diffusion components with various approaches.

a sample of one million text prompts from the LAION-400M dataset was used for textual projection training and experiments.

this is the dataset guage for the domain of CXR, we leverage the publicly available MIMIC-CXR dataset [15], under institutional review board approval. The full dataset contains 377,110 images and their associated radiology reports, from 227,827 unique studies performed at the Beth Israel Deaconess Medical Center in Boston, MA, USA.

Components:
1. LAION-5B pretrained variational autoencoder (VAE)
2. A frozen CLIP text encoder
3. Textual inversion
4. Fine-tuning the U-Net component

## 2. Textural Inversion
An Image is Worth One Word: Personalizing Text-to-Image Generation using Textual Inversion: https://arxiv.org/abs/2208.01618