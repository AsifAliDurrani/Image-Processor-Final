from image_preprocessor_ml import resize_image, remove_background

# Resize
resize_image("input.jpg", "resized.jpg", (300, 300))

# Remove background
remove_background("input.jpg", "no_bg.png")