import mss
from PIL import Image
import numpy as np
from ultralytics import YOLO
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from ..functions import screenshot_health_area

# Load the YOLOv8 model
model_path = os.path.join(os.path.dirname(__file__), 'health.pt')
model = YOLO(model_path)

# Convert screenshot to YOLO input format and run inference
def detect_health_in_screenshot():
    # Take screenshot
    img = screenshot_health_area()

    # Convert to numpy array for YOLO input
    img = np.array(img)

    # Run inference with specified confidence threshold
    results = model(img)  # Adjust threshold as needed

    # Define class names based on YAML
    class_names = ['alive', 'dead']

    # Iterate over detections and check if 'dead' is found
    for result in results[0].boxes:
        class_id = int(result.cls)  # Get class ID
        confidence = result.conf  # Get confidence for the detection
        class_name = class_names[class_id]  # Map to class name
        
        if class_name == 'dead':
            print(f"Detected 'dead' with confidence {confidence}")
            return True

    print("No 'dead' detected")
    return False
