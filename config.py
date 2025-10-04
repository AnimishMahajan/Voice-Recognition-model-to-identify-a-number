import os

# Paths
DATA_DIR = os.path.join("data", "processed")
MODEL_DIR = "models"
os.makedirs(MODEL_DIR, exist_ok=True)

# Training parameters
BATCH_SIZE = 8
EPOCHS = 100
LEARNING_RATE = 0.1
IMG_SIZE = (64, 64)
NUM_CLASSES = 10
