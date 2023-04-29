# Models and Training Options
## 1. Stanford Pipeline
Experiments were conducted on 64 A100 GPUs split across two compute instances. Models were mostly trained (unless otherwise specified) in bf16 precision, as this led to 1/3 reduction of training time. Using bf16 precision, no significant training time difference was noticed across the various experiments, whether they fine-tuned one or several SD components, except when changing the number of training steps itself. At an image resolution of 512x512 px, an A100 GPU fine-tuning SD can hold a batch size of 8 (bf16 precision). Splitting batches across the GPUs of each compute instance, models were trained with a batch size of 256. In this setting, fine-tuning a model for 1k training steps took approximately 20 minutes; for 12.5k training steps, around 5 hours; for 60k training steps, one day.

Model weights for the SD pipeline (version 1.4) were obtained from the repository ”CompVis/stable-diffusionv1-4”(Hugging Face hub [53]), unless otherwise specified.

The code implementation was built on both the diffusers library [50] and the ViLMedic library [8]. Two domainspecific text encoders were used: RadBERT [4], downloadable on the HuggingFace repo StanfordAIMI/RadBERT, and SapBERT [20] available at cambridgeltl/SapBERTfrom-PubMedBERT-fulltext. In the experiments that follow, guidance scale 4 and 75 inference steps with a PNDM noise scheduler [21] enabled the generation of synthetic images properly conditioned on the associated prompts.

this is the datazset guage for the domain of CXR, we leverage the publicly available MIMIC-CXR dataset [15], under institutional review board approval. The full dataset contains 377,110 images and their associated radiology reports, from 227,827 unique studies performed at the Beth Israel Deaconess Medical Center in Boston, MA, USA.

