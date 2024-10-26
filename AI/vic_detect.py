import mss
from PIL import Image
import numpy as np
from ultralytics import YOLO
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from functions import screenshot

# Load the YOLOv8 model
model_path = os.path.join(os.path.dirname(__file__), 'vic.pt')
model = YOLO(model_path)


# Convert screenshot to YOLO input format and run inference
def detect_vic_in_screenshot():
    # Take screenshot
    img = screenshot()

    # Convert to numpy array for YOLO input
    img = np.array(img)

    # Run inference
    results = model(img)

    # Iterate over detections and check if 'vic' or 'vic_gifted' is found
    found_vic = False
    found_vic_gifted = False
    class_names = ['vic', 'vic_gifted']

    for result in results[0].boxes:
        class_id = int(result.cls)  # Get class ID
        class_name = class_names[class_id]  # Map to class name
        
        if class_name == 'vic':
            print("Detected: vic")
            found_vic = True
        elif class_name == 'vic_gifted':
            print("Detected: vic_gifted")
            found_vic_gifted = True
    
    if not found_vic and not found_vic_gifted:
        print("No vic or vic_gifted found.")
        return False
    else:
        return True
