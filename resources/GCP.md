## VM Instances:
https://console.cloud.google.com/compute/instances?project=distributed-eye-384021

https://console.cloud.google.com/compute/instances?authuser=2&project=distributed-eye-384021

## Buckets:
https://console.cloud.google.com/storage/browser?authuser=2&project=distributed-eye-384021&prefix=&forceOnBucketsSortingFiltering=true

## VS Code:
Follow this guide to SSH into the VM instance and use VS Code:.
https://towardsdatascience.com/complete-walkthrough-to-connect-your-sde-to-gcp-with-github-bc39eec0db9e

## Mounting Bucket to GCE VM:
[Mount a Cloud Storage bucket using Cloud Storage FUSE](https://cloud.google.com/storage/docs/gcsfuse-quickstart-mount-bucket)
https://github.com/GoogleCloudPlatform/gcsfuse/blob/master/docs/mounting.md
**Note:** Does not work on Colab-vm
```bash
mkdir "$HOME/mount-folder"
gcsfuse cxray_dataset "$HOME/mount-folder"
```
Accessing Files:
```bash
gcloud storage <command> gs://cxray_dataset/<dir name>
# example 1: listing files in a dir
gcloud storage ls gs://cxray_dataset/padchest
# example 2: moving a folder from bucket to local
gcloud storage cp -r gs://cxray_dataset/padchest/padchest_sample2 padchest
```
**IMPORTANT:** REMEMBER TO UNMOUNT THE BUCKET AFTER USE
```bash
fusermount -u "$HOME/mount-folder"
```
## Transferring data from GCE VM to Bucket:
```
gsutil -m cp -r <src_dir> gs://<bucket_name>/<dest_dir>
```
Example:
```
gsutil -m cp -r /home/aaz7118_nyu_edu/tests/ gs://cxray_dataset/
```
## Transferring data between Google Drive and Google Cloud Storage using Google Colab
https://philipplies.medium.com/transferring-data-from-google-drive-to-google-cloud-storage-using-google-colab-96e088a8c041
## WebUI

### Installation:
create a new conda env and activate it
```bash
conda create --name webui python=3.10.6
conda activate webui
```
1. Install the dependencies:
```bash
sudo apt install wget git python3 python3-venv
```
2. Navigate to the directory you would like the webui to be installed and execute the following command:
```bash
bash <(wget -qO- https://raw.githubusercontent.com/AUTOMATIC1111/stable-diffusion-webui/master/webui.sh)
```
3. Run `webui.sh`.
4. Check `webui-user.sh` for options.
5. Click the link generated on the terminal

### Running
```bash
conda activate webui
cd stable-diffusion-webui
./webui.sh
```
Click the link generated on the terminal

## Transfer Billing Account
https://cloud.google.com/billing/docs/how-to/modify-project#change_the_billing_account_for_a_project

https://cloud.google.com/billing/docs/how-to/modify-project#how-to-change-ba

https://cloud.google.com/billing/docs/how-to/modify-project#required-permissions-change

On the project: Project Billing Manager + Project Viewer OR Project Owner

AND

On the current and target Cloud Billing account: Billing Account User + Billing Account Viewer OR Billing Account Administrator
