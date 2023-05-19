import os
import sys

LABEL_PATH = "PADCHEST_chest_x_ray_images_labels_160K_01.02.19.csv"

def main(src_dir, dst_dir, ImageDir=None, labels=LABEL_PATH):
    process_prompts(src_dir, dst_dir, labels=labels, ImageDir=ImageDir)
    convert_to_RGB(src_dir, dst_dir)
        
def process_prompts(src_dir, dst_dir, labels, ImageDir=None):
    return

def convert_to_RGB(src_dir, dst_dir):
    return

if __name__ == 'main':
    src_dir = sys.argv[1]
    des_dir = sys.argv[2]
    if len(sys.argv) > 3:
        ImageDir = sys.argv[3]
    else:
        ImageDir = None
    if len(sys.argv) > 4:
        labels = sys.argv[4]
    main(src_dir, des_dir, ImageDir=ImageDir, labels=labels)