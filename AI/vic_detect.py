import mss
from PIL import Image
import numpy as np
from ultralytics import YOLO
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from functions import *

# Check beesmas toggle and load appropriate model
try:
    beesmas_enabled = int(readFile("guiFiles/beesmasToggle.txt"))
except:
    beesmas_enabled = 0

# Load model based on toggle
if beesmas_enabled:
    model_path = os.path.join(os.path.dirname(__file__), 'vic_beesmas.pt')
else:
    model_path = os.path.join(os.path.dirname(__file__), 'vic_plain3.pt')

model = YOLO(model_path)

# Convert screenshot to YOLO input format and run inference
def detectVicBee(img):
    # Convert to numpy array for YOLO input
    img = np.array(img)

    img = img[..., ::-1]
    
    sendScreenshot("Checking vic bee")

    # Run inference
    results = model(img, conf=0.3)

    class_names = ['vic', 'vic_gifted', 'vic_under']

    poses = []

    for result in results[0].boxes:
        class_id = int(result.cls)  # Get class ID
        class_name = class_names[class_id]  # Map to class name

        x_min, y_min, x_max, y_max = result.xyxy[0].cpu().numpy().tolist()  # Assuming xyxy format is [x_min, y_min, x_max, y_max]

        # Calculate center
        pos = [(x_min + x_max) / 2, (y_min + y_max) / 2]

        poses.append(pos)

        print(f"Detected: {class_name}, at pos {pos}")
        
        sendScreenshot("Found vic bee!")

    return len(poses) > 0

