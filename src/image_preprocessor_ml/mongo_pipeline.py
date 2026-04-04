from pymongo import MongoClient
from image_preprocessor_ml import remove_background,resize_image
from PIL import Image
import io
from urllib.parse import quote_plus

username = "Asif"
password = "Asif@5815"

username = quote_plus("asif")
password = quote_plus("asif@123")

# 🔹 MongoDB Connection (paste your Atlas string)
MONGO_URI = "mongodb+srv://{username}:{password}@cluster0.fjcdh3v.mongodb.net/"

client = MongoClient(MONGO_URI)
db = client["image_database"]
collection = db["processed_images"]


def save_images_to_mongodb(original_path, processed_path, filename):
    with open(original_path, "rb") as f:
        original_bytes = f.read()

    with open(processed_path, "rb") as f:
        processed_bytes = f.read()

    document = {
        "filename": filename,
        "original_image": original_bytes,
        "processed_image": processed_bytes,
    }

    collection.insert_one(document)
    print("✅ Images saved to MongoDB")


def retrieve_and_save_image(filename):
    doc = collection.find_one({"filename": filename})

    image_bytes = doc["processed_image"]
    image = Image.open(io.BytesIO(image_bytes))
    image.save("retrieved_no_bg.png")

    print("✅ Retrieved image saved as retrieved_no_bg.png")


if __name__ == "__main__":
    input_image = "input.jpg"

    # Process using your package
    resize_image(input_image, "resized.jpg", (300, 300))
    remove_background(input_image, "no_bg.png")

    # Save to MongoDB
    save_images_to_mongodb(input_image, "no_bg.png", "input.jpg")

    # Retrieve back from MongoDB
    retrieve_and_save_image("input.jpg")