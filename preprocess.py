import os
import sys
import pandas as pd
import argparse

LABEL_PATH = "padchest/PADCHEST_chest_x_ray_images_labels_160K_01.02.19.csv"

def parse_args():
    parser = argparse.ArgumentParser(description='Preprocess PADCHEST dataset')
    parser.add_argument(
        '-src',
        '--src_dir',
        help='Source directory of images',
        type=str, 
        required=True,
        )
    parser.add_argument(
        '-dst',
        '--dst_dir',
        help='Destination directory of pre-processed images and text files',
        type=str,
        required=True,
        )
    parser.add_argument(
        '-l',
        '--labels',
        help='Path to labels csv file',
        type=str,
        default=LABEL_PATH,
        )
    parser.add_argument(
        '-dir',
        '--img_dir',
        help='Image directory name',
        type=int,
        default=None,
        )
        

def process_prompts(src_dir, dst_dir, labels, ImageDir=None):
    
    labels = pd.read_csv(labels, index_col=0)
    
    # filter the PD for the ImageDir
    if ImageDir:
        labels = labels[labels['ImageDir'] == ImageDir]

    # Calculate age, If PatientBirth is NA, age is NA otherwise age is year - birth
    labels['birth'] = labels['PatientBirth']
    labels['year'] = labels['StudyDate_DICOM'].astype(str).str[:4].astype(int)
    labels['age'] = (labels['year'] - labels['birth']).astype('Int64')

    # Generate prompts
    labels['age_prompt'] = labels['age'].apply(lambda x: '' if pd.isna(x) else 'age ' + str(x))
    labels['sex_prompt'] = labels['PatientSex_DICOM'].apply(lambda x: ' male, ' if x == 'M' else ' female, ' if x == 'F' else ', ')
    labels['view_prompt'] = labels['ViewPosition_DICOM'].apply(lambda x: '' if pd.isna(x) else 'view ' + str(x) + ', ')
    labels['projection_prompt'] = labels['Projection'].apply(lambda x: '' if pd.isna(x) else 'projection ' + str(x) + ', ')
    labels['modality_prompt'] = labels['Modality_DICOM'].apply(lambda x: '' if pd.isna(x) else 'modality ' + str(x) + ', ')
    labels['diagnosis_prompt'] = labels['LabelsLocalizationsBySentence'].apply(lambda x: '' if pd.isna(x) else 'diagnosis ' + str(x))
    labels['Prompt'] = 'Chest X-ray, ' + labels['age_prompt'] + labels['sex_prompt'] + labels['view_prompt'] + labels['projection_prompt'] + labels['modality_prompt'] + labels['diagnosis_prompt']
    # Remove square brackets and single quotes
    labels['Prompt'] = labels['Prompt'].str.replace('[', '').str.replace(']', '').str.replace("'", '')
    # Save a csv file with 3 columns, ImageID, ImageDir, and Prompt
    labels[['ImageID', 'ImageDir', 'Prompt']].to_csv(os.join(dst_dir, 'PADCHEST_Prompt.csv'), index=False)
    
    # Save txt files with prompts as the same name as the image file at the destination directory
    for image in os.listdir(src_dir):
        if image in labels['ImageID'].values:
            prompt = labels[labels['ImageID'] == image]['Prompt'].values[0]
            with open(os.join(dst_dir, image.split('.')[0] + '.txt'), 'w') as f:
                f.write(prompt)
            

def convert_to_RGB(src_dir, dst_dir):
    return

if __name__ == 'main':
    args - parse_args()
    process_prompts(src_dir=args.src_dir, dst_dir=args.dst_dir, labels=args.labels, ImageDir=args.img_dir)