from PIL import Image
import cv2

def jpeg(name,q):
    # Open the input image
    input_image_path = name
    output_compressed_image_path = "compressed.jpg"
    
    # Open the image using Pillow
    image = Image.open(input_image_path)
    
    # Set the compression quality (0-100, higher is better quality)
    compression_quality = q  # Adjust this as needed
    
    # Save the image in JPEG format with the specified quality
    image.save(output_compressed_image_path, "JPEG", quality=compression_quality)
    
    # Close the image
    image.close()
    img=cv2.imread('compressed.jpg')
    return img
def file(inputimage,q):
    img=jpeg(inputimage,q)
    return img