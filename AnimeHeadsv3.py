import collections
import json
import os
import datasets

ANNOTATION_FILENAME = "_annotations.coco.json"

class AHv3Config(datasets.BuilderConfig):
    def __init__(self, data_urls, **kwargs):
        super(AHv3Config, self).__init__(**kwargs)
        self.data_urls = data_urls

class AHv3(datasets.GeneratorBasedBuilder):
    BUILDER_CONFIGS = [
        AHv3Config(name="With augmentation", data_urls={"train": "AHv3-AUG/train.zip", "validation": "AHv3-AUG/valid.zip", "test": "AHv3-AUG/test.zip"}),
        AHv3Config(name="Without augmentation", data_urls={"train": "AHv3-NA/train.zip", "validation": "AHv3-NA/valid.zip", "test": "AHv3-NA/test.zip"}),
    ]

    def _info(self):
        features = datasets.Features({"image_id": datasets.Value("int64"), "image": datasets.Image(), "width": datasets.Value("int32"), "height": datasets.Value("int32"), "objects": datasets.Sequence({"id": datasets.Value("int64"), "area": datasets.Value("int64"), "bbox": datasets.Sequence(datasets.Value("float32"), length=4), "category": datasets.Value("string")})})
        return datasets.DatasetInfo(features=features)

    def _split_generators(self, dl_manager):
        data_files = dl_manager.download_and_extract(self.config.data_urls)
        return [datasets.SplitGenerator(name=datasets.Split.TRAIN, gen_kwargs={"folder_dir": data_files["train"]}), datasets.SplitGenerator(name=datasets.Split.VALIDATION, gen_kwargs={"folder_dir": data_files["validation"]}), datasets.SplitGenerator(name=datasets.Split.TEST, gen_kwargs={"folder_dir": data_files["test"]})]

    def _generate_examples(self, folder_dir):
        def process_annot(annot, category_id_to_category):
            return {"id": annot["id"], "area": annot["area"], "bbox": annot["bbox"], "category": category_id_to_category[annot["category_id"]]}

        image_id_to_image = {}
        idx = 0

        annotation_filepath = os.path.join(folder_dir, ANNOTATION_FILENAME)
        with open(annotation_filepath, "r") as f:
            annotations = json.load(f)
        category_id_to_category = {category["id"]: category["name"] for category in annotations["categories"]}
        image_id_to_annotations = collections.defaultdict(list)
        for annot in annotations["annotations"]:
            image_id_to_annotations[annot["image_id"]].append(annot)
        filename_to_image = {image["file_name"]: image for image in annotations["images"]}

        for filename in os.listdir(folder_dir):
            filepath = os.path.join(folder_dir, filename)
            if filename in filename_to_image:
                image = filename_to_image[filename]
                objects = [process_annot(annot, category_id_to_category) for annot in image_id_to_annotations[image["id"]]]
                with open(filepath, "rb") as f:
                    image_bytes = f.read()
                yield idx, {"image_id": image["id"], "image": filepath, "height": image["height"], "width": image["width"], "objects": objects}
                idx += 1
