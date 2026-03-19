from PIL import Image

def resize_image(input_path, output_path, size=(256, 256)):
    img = Image.open(input_path)
    img = img.resize(size)
    img.save(output_path)
    return output_path