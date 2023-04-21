---
task_categories:
- object-detection
license: wtfpl
---
# AnimeHeadsv3 Object Detection Dataset

The AnimeHeadsv3 Object Detection Dataset is a collection of anime and art images, including manga pages, that have been annotated with object bounding boxes for use in object detection tasks. This dataset was used to train the final version of the [Anime Object Detection Models](https://huggingface.co/nyuuzyou/AnimeHeads).

## Contents

The dataset contains a total of 8037 images, split into training, validation, and testing sets. The images were collected from various sources and include a variety of anime and art styles, including manga.

The annotations were created using the COCO format, with each annotation file containing the bounding box coordinates and label for each object in the corresponding image. The dataset has only one class named "head".

Augmentation parameters:

    Outputs per training example: 3
    Flip: Horizontal
    Saturation: Between -40% and +40%
    Blur: Up to 4px
    Noise: Up to 4% of pixels
