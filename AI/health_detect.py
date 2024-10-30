import numpy as np
from ultralytics import YOLO
import os
import sys
import time
import keyboard
from functions import screenshot

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# Load the YOLOv8 model
model_path = os.path.join(os.path.dirname(__file__), 'health.pt')
model = YOLO(model_path)


# Convert screenshot to YOLO input format and run inference
def detect_health_in_screenshot():

    img = screenshot()
    # Convert to numpy array for YOLO input
    img = np.array(img)

    img = img[..., ::-1]

    # Run inference
    results = model(img, conf=0.65)

    class_names = ['dead', 'alive']

    poses = []

    for result in results[0].boxes:
        class_id = int(result.cls)  # Get class ID
        class_name = class_names[class_id]  # Map to class name

        x_min, y_min, x_max, y_max = result.xyxy[0].cpu().numpy().tolist()  # Assuming xyxy format is [x_min, y_min, x_max, y_max]

        # Calculate center
        pos = [(x_min + x_max) / 2, (y_min + y_max) / 2]

        poses.append(pos)

        if class_name == 'dead':
            print(f"Detected: alive, at pos {pos}")

            return True

        elif class_name == 'alive':
            print(f"Detected: dead, at pos {pos}")


    return True

