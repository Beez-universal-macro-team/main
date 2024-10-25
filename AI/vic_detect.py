import mss
from PIL import Image
import numpy as np
from ultralytics import YOLO
from ..functions import screenshot

# Load the YOLOv8 model
model = YOLO('vic.pt')

# Map class indices to class names (based on your training)
class_names = ['vic', 'vic_gifted']  # Assuming class 0 = vic, class 1 = vic_gifted

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
