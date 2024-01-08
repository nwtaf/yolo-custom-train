import random
import numpy as np
from PIL import Image, ImageDraw
from pathlib import Path

def plot_bounding_box(image, annotation_list, class_id_to_name_mapping):
    annotations = np.array(annotation_list)
    w, h = image.size
    
    plotted_image = ImageDraw.Draw(image)

    for ann in annotations:
        obj_cls, x_center, y_center, width, height = ann
        obj_cls = int(obj_cls)

        # Transform the bbox coordinates to pixel values
        x_center *= w
        y_center *= h
        width *= w
        height *= h

        # Compute the top-left and bottom-right coordinates
        x1 = x_center - (width / 2)
        y1 = y_center - (height / 2)
        x2 = x_center + (width / 2)
        y2 = y_center + (height / 2)

        # Draw the bbox
        plotted_image.rectangle(((x1, y1), (x2, y2)), outline="red")

        # Draw the class name
        plotted_image.text((x1, y1 - 10), class_id_to_name_mapping[obj_cls], fill="red")

    image.show()

# Get a list of all annotation files
annotation_files = list(Path('data/labels/test/').glob('*.txt'))

# Select a random base name
base_name = random.choice([file.stem for file in annotation_files])

# Construct the paths to the annotation file and the image file
annotation_file = Path('data/labels/test/') / f'{base_name}.txt'
image_file = Path('data/images/test/') / f'{base_name}.png'

# Check if the annotation file exists
if not annotation_file.exists():
    print(f"Oops, annotation file {annotation_file} doesn't exist!")
else:
    with open(annotation_file, 'r') as file:
        print(file.read())

# Check if the image file exists
if not image_file.exists():
    print(f"Oops, image file {image_file} doesn't exist!")
else:
    # Load the image
    image = Image.open(image_file)

# Define the class_name_to_id_mapping dictionary
class_name_to_id_mapping = {'apple_tree': 0}

# Create a reverse mapping from class IDs to class names
class_id_to_name_mapping = dict(zip(class_name_to_id_mapping.values(), class_name_to_id_mapping.keys()))

# Read the annotation file
with open(annotation_file, 'r') as file:
    annotation_list = [list(map(float, line.strip().split())) for line in file.readlines()]

# Plot the image with bounding boxes
plot_bounding_box(image, annotation_list, class_id_to_name_mapping)
