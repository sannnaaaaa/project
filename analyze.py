import cv2
import numpy as np


def analyze_soil(image_path):

    # Read image
    image = cv2.imread(image_path)

    # Resize image
    image = cv2.resize(image, (300, 300))

    # Convert to RGB
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Calculate average color
    avg_color = rgb.mean(axis=0).mean(axis=0)

    r, g, b = avg_color

    # Simple soil detection logic
    if r < 80 and g < 80 and b < 80:
        soil_type = "Black Soil"

    elif r > 150 and g > 120 and b < 100:
        soil_type = "Red Soil"

    elif r > 170 and g > 170 and b > 120:
        soil_type = "Sandy Soil"

    else:
        soil_type = "Loamy Soil"

    return soil_type