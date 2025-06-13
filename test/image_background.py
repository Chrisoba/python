# remove image background
from rembg import remove
from PIL import Image
def remove_background(input_image_path: str, output_image_path: str) -> None:
    """
    Remove the background from an image and save the result.

    :param input_image_path: Path to the input image file.
    :param output_image_path: Path to save the output image file.
    """
    input_image = Image.open(input_image_path)
    output_image = remove(input_image)
    output_image.save(output_image_path)    

# Example usage:
# remove_background('input_image.png', 'output_image.png')
if __name__ == "__main__":
    # Example usage
    remove_background('input_image.png', 'output_image.png')
    print("Background removed and saved to output_image.png")
# Note: Ensure you have the 'rembg' and 'Pillow' libraries installed in your Python environment.

# Another example usage:
input_image_path = 'input_image.png'
output_image_path = 'output_image.png'
input_image = Image.open(input_image_path)
output_image = remove(input_image)
output_image.save(output_image_path)