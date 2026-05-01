import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import json
import cv2

# Load model
model = tf.keras.models.load_model("model/disease_model.h5")

# Load classes
with open("model/classes.json") as f:
    classes = json.load(f)

IMG_SIZE = 128

# =========================
# GREEN COLOR CHECK (NEW 🔥)
# =========================
def has_enough_green(img_path):
    img = cv2.imread(img_path)
    img = cv2.resize(img, (128, 128))

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Green range
    lower_green = np.array([25, 40, 40])
    upper_green = np.array([90, 255, 255])

    mask = cv2.inRange(hsv, lower_green, upper_green)

    green_pixels = np.sum(mask > 0)
    total_pixels = mask.size

    green_ratio = green_pixels / total_pixels

    # 🔥 Threshold (tune here if needed)
    return green_ratio > 0.10


# =========================
# SMART TREATMENT FUNCTION
# =========================
def get_treatment(disease_name):
    disease_name = disease_name.lower()

    if "healthy" in disease_name:
        return "No disease detected. Maintain proper watering and sunlight."

    if "blight" in disease_name:
        return "Apply Mancozeb or Chlorothalonil. Remove infected leaves."

    if "rust" in disease_name:
        return "Use sulfur fungicide and improve airflow."

    if "scab" in disease_name:
        return "Apply Captan fungicide and remove infected leaves."

    if "spot" in disease_name:
        return "Use copper fungicide. Avoid overhead watering."

    if "mildew" in disease_name:
        return "Apply sulfur spray and improve ventilation."

    if "rot" in disease_name:
        return "Remove infected parts and reduce moisture."

    if "mosaic" in disease_name or "virus" in disease_name:
        return "Remove infected plants and control insects."

    if "yellow" in disease_name or "curl" in disease_name:
        return "Control whiteflies using neem oil."

    if "bacterial" in disease_name:
        return "Use copper bactericide."

    return "Maintain proper plant care and use general fungicide."


# =========================
# PREDICTION FUNCTION
# =========================
def predict_image(img_path):
    # 🔥 STEP 1: GREEN CHECK
    if not has_enough_green(img_path):
        return "No leaf detected ❌", 0, "Image does not contain enough green content."

    # Load image
    img = image.load_img(img_path, target_size=(IMG_SIZE, IMG_SIZE))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    preds = model.predict(img_array)[0]

    class_index = np.argmax(preds)
    confidence = float(np.max(preds))
    predicted_class = classes[class_index].lower()

    # 🔥 STEP 2: CONFIDENCE CHECK
    if confidence < 0.80:
        return "No leaf detected ❌", confidence, "Low confidence prediction."

    # 🔥 STEP 3: KEYWORD CHECK
    leaf_keywords = [
        "apple", "tomato", "potato", "corn", "grape",
        "healthy", "blight", "spot", "rust",
        "mildew", "rot", "scab"
    ]

    if not any(word in predicted_class for word in leaf_keywords):
        return "No leaf detected ❌", confidence, "Invalid plant image."

    # HEALTHY
    if "healthy" in predicted_class:
        return "Healthy Leaf ✅", confidence, get_treatment(predicted_class)

    # DISEASE
    treatment = get_treatment(predicted_class)
    return predicted_class, confidence, treatment