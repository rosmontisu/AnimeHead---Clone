---
task_categories:
- object-detection
license: wtfpl
dataset_info:
- config_name: With augmentation
  features:
  - name: image_id
    dtype: int64
  - name: image
    dtype: image
  - name: width
    dtype: int32
  - name: height
    dtype: int32
  - name: objects
    sequence:
    - name: id
      dtype: int64
    - name: area
      dtype: int64
    - name: bbox
      sequence: float32
      length: 4
    - name: category
      dtype: string
  splits:
  - name: train
    num_bytes: 2817954
    num_examples: 8037
  - name: validation
    num_bytes: 37647
    num_examples: 100
  - name: test
    num_bytes: 8425
    num_examples: 20
  download_size: 590150250
  dataset_size: 2864026
- config_name: Without augmentation
  features:
  - name: image_id
    dtype: int64
  - name: image
    dtype: image
  - name: width
    dtype: int32
  - name: height
    dtype: int32
  - name: objects
    sequence:
    - name: id
      dtype: int64
    - name: area
      dtype: int64
    - name: bbox
      sequence: float32
      length: 4
    - name: category
      dtype: string
  splits:
  - name: train
    num_bytes: 932413
    num_examples: 2659
  - name: validation
    num_bytes: 37647
    num_examples: 100
  - name: test
    num_bytes: 7393
    num_examples: 18
  download_size: 512953012
  dataset_size: 977453
---

# AnimeHeadsv3 Object Detection Dataset

The AnimeHeadsv3 Object Detection Dataset is a collection of anime and art images, including manga pages, that have been annotated with object bounding boxes for use in object detection tasks.
## Contents

There are two versions of the dataset available:
The dataset contains a total of 8157 images, split into training, validation, and testing sets. The images were collected from various sources and include a variety of anime and art styles, including manga.

- Dataset with augmentation: Contains 8157 images.
- Dataset without augmentation: Contains 2777 images.

The images were collected from various sources and include a variety of anime and art styles, including manga. The annotations were created using the COCO format, with each annotation file containing the bounding box coordinates and label for each object in the corresponding image. The dataset has only one class named "head".

## Preprocessing

The dataset with augmentation has the following preprocessing parameters:

    Resize: Fit within 640x640

The dataset without augmentation does not have any preprocessing applied.

## Augmentation Parameters

The following augmentation parameters were applied to the dataset with augmentation:

    Outputs per training example: 3
    Flip: Horizontal
    Saturation: Between -40% and +40%
    Blur: Up to 4px
    Noise: Up to 4% of pixels
