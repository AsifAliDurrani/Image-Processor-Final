from setuptools import setup, find_packages

setup(
    name="image_preprocessor_ml",
    version="0.2",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "Pillow",
        "rembg"
    ],
    author="Asif Durrani",
    description="Image preprocessing package for ML pipelines",
)
entry_points={
    "console_scripts": [
        "imgproc=image_preprocessor_ml.resize:resize_image",
    ],
}