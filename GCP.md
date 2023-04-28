## VM Instances:
https://console.cloud.google.com/compute/instances?project=distributed-eye-384021
https://console.cloud.google.com/compute/instances?authuser=2&project=distributed-eye-384021

## Buckets:
https://console.cloud.google.com/storage/browser?authuser=2&project=distributed-eye-384021&prefix=&forceOnBucketsSortingFiltering=true

## Mounting Bucket to GCE VM:
[Mount a Cloud Storage bucket using Cloud Storage FUSE](https://cloud.google.com/storage/docs/gcsfuse-quickstart-mount-bucket)
**Note:** Does not work on Colab-vm
```bash
gcsfuse cxray_dataset "$HOME/mount-folder"
```
Accessing Files:
```bash
gcloud storage <command> gs://cxray_dataset/<dir name>
# example 1: listing files in a dir
gcloud storage ls gs://cxray_dataset/padchest
# example 2: moving a folder from bucket to local
gcloud storage cp -r gs://cxray_dataset/padchest/padchest_sample2 padches
```
