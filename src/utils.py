import os

def validate_path(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"{path} not found")