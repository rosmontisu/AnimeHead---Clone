---
task_categories:
- object-detection
---
# AnimeHeadsv3 Object Detection Dataset

The AnimeHeadsv3 Object Detection Dataset is a collection of anime and art images, including manga pages, that have been annotated with object bounding boxes for use in object detection tasks. This dataset was used to train the final version of the [Anime Object Detection Models](https://huggingface.co/nyuuzyou/AnimeHeads).

## Contents

The dataset contains a total of 8037 images, split into training, validation, and testing sets. The images were collected from various sources and include a variety of anime and art styles, including manga.

The annotations were created using the YOLO format, with each annotation file containing the bounding box coordinates and label for each object in the corresponding image. Dataset has only one class named "head".

## Usage

To use this dataset for object detection tasks, you can download the dataset files and annotations and use them to train your own object detection model. The annotation files are provided in the YOLO format, which can be used with popular object detection frameworks such as YOLOv5 and YOLOv8. 
