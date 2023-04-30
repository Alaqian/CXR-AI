# Models and Training Options
## 1. Stanford (Original Chest X-ray Study)
Adapting Pretrained Vision-Language Foundational
Models to Medical Imaging Domains https://arxiv.org/pdf/2210.04133.pdf

RoentGen: Vision-Language Foundation Model for Chest X-ray Generation https://arxiv.org/pdf/2211.12737.pdf

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

### Approaches:
1. LAION-5B pretrained variational autoencoder (VAE)
2. A frozen CLIP text encoder
3. Textual inversion
4. Fine-tuning the U-Net component

### Results:
1. Out of all the methods, the U-Net fine-tuning seems by far the most promising: it gets the lowest
FID-scores and obviously the most realistic outputs. further progress in the domain-specific generation of images for radiology require
the use of more domain-specific metrics, that would be able to capture the ability of the model to
correctly insert abnormalities that are coherent with the conditioning text prompt.

2. fine-tuning both the U-Net and CLIP (Contrastive Language Image Pre-Training [35]) text encoder yields the the
highest image fidelity and conceptual correctness.

3. The original CLIP text encoder can be replaced with
a domain-specific text encoder that leads to improved
performance. In the setting where the text encoder is kept frozen and only the U-Net is trained.

4. RoentGen can be fine-tuned on a small subset (1.1-
5.5k) of images and prompts for use as a data augmentation tool for downstream image classification tasks. 

## 2. Textural Inversion
An Image is Worth One Word: Personalizing Text-to-Image Generation using Textual Inversion: https://arxiv.org/abs/2208.01618

Textual Inversion, Personalizing Text-to-Image Generation https://invoke-ai.github.io/InvokeAI/features/TEXTUAL_INVERSION/

How to Fine-tune Stable Diffusion using Textual Inversion How to Fine-tune Stable Diffusion using Textual Inversion https://towardsdatascience.com/how-to-fine-tune-stable-diffusion-using-textual-inversion-b995d7ecc095

The Stable Diffusion model can be fine-tuned to generate
better looking images for the radiology setting by focusing on the embeddings of the text encoder.
In this case, during training, the VAE, the U-Net, as well as all the other layers of the text encoder
are frozen. In addition, a new token gets introduced, that can either describe: patient-level features,
such as gender, age and body weight; procedure-level features, such as body part and modality;
abnormality-level features, such as "no findings" or "pleural effusion".

As an example, we could introduce the token < lung − xray > that is supposed to describe both a
body part, lungs, and a modality, X-ray. This learning approach, denoted Textual Inversion, zeroes
out all the gradients associated with the embeddings of the already existing tokens, and in the end
only learns the embedding of this newly introduced token.

Did not yield good results in the original paper. A more complex architecture,
instead of a simple 1-hidden-layer projection, could be worth exploring: if projection-based domain-adaptation turns out to produce interesting examples, this could open the door to quick domain-adaptation for the large amount of pre-trained text encoders that are now available.

## 3. DreamBooth U-Net Fine-tuning
DreamBooth: Fine Tuning Text-to-Image Diffusion Models for Subject-Driven Generation https://arxiv.org/abs/2208.12242

Improve the baseline Stable Diffusion model to generate better domain-specific images by fine-tuning the U-Net. All components except the U-net are kept frozen. The training is similar to the training of the original Stable Diffusion model, relying on MSE loss at several time steps of the denoising process to progressively converge to better generation of in-domain images.
