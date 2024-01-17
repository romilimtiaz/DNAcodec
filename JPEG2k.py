import cv2
from PIL import Image
import numpy as np

def save_as_jpeg2000(image_path, quality_level):
    # Read the image using OpenCV
    img = cv2.imread(image_path)

    # Convert the image from BGR to RGB format (OpenCV uses BGR by default)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Convert the image to a PIL Image
    pil_img = Image.fromarray(img_rgb)

    # Save the image in JPEG 2000 format
    # Quality level is a number between 1-100 (higher means better quality)
    pil_img.save('output_image.jp2', 'JPEG2000', quality_mode='rates', quality_layers=[quality_level])

# Usage
input_image_path = 'tengyart-kSvpTrfhaiU-unsplash.jpg'  # Path to your input image
save_as_jpeg2000(input_image_path)

