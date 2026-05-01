treatments = {

# 🍎 APPLE
"Apple Black Rot": "Remove infected fruits and leaves. Apply fungicides like captan or myclobutanil.",
"Apple Cedar Rust": "Use resistant varieties and apply fungicides like sulfur or myclobutanil.",
"Apple Healthy": "No treatment needed. Maintain proper watering and fertilization.",
"Apple Scab": "Apply fungicides such as captan or sulfur. Remove infected leaves.",

# 🌽 CORN
"Corn Cercospora Gray Leaf Spot": "Use resistant hybrids and apply fungicides like azoxystrobin.",
"Corn Common Rust": "Apply fungicides and use resistant varieties.",
"Corn Healthy": "No treatment needed.",
"Corn Northern Leaf Blight": "Use resistant hybrids and crop rotation.",

# 🍅 TOMATO
"Tomato Early Blight": "Remove infected leaves and apply fungicides like chlorothalonil.",
"Tomato Late Blight": "Use copper fungicides and avoid overhead watering.",
"Tomato Healthy": "No treatment needed.",
"Tomato Bacterial Spot": "Use copper-based bactericides and disease-free seeds.",
"Tomato Leaf Mold": "Improve air circulation and apply fungicides.",
"Tomato Mosaic Virus": "Remove infected plants and control insects.",
"Tomato Septoria Leaf Spot": "Apply fungicides and remove infected leaves.",
"Tomato Spider Mites Two Spotted Spider Mite": "Use neem oil or insecticidal soap.",
"Tomato Target Spot": "Apply fungicides and remove infected debris.",
"Tomato Yellow Leaf Curl Virus": "Control whiteflies and remove infected plants.",

# 🥔 POTATO
"Potato Early Blight": "Apply fungicides and practice crop rotation.",
"Potato Late Blight": "Use certified seeds and fungicides like mancozeb.",
"Potato Healthy": "No treatment needed.",

# 🍇 GRAPE
"Grape Black Rot": "Remove infected berries and apply fungicides.",
"Grape Esca Black Measles": "Prune infected wood and improve vineyard sanitation.",
"Grape Healthy": "No treatment needed.",
"Grape Leaf Blight Isariopsis Leaf Spot": "Apply fungicides and remove infected leaves.",

# 🍓 STRAWBERRY
"Strawberry Healthy": "No treatment needed.",
"Strawberry Leaf Scorch": "Remove infected leaves and improve spacing.",

# 🍑 PEACH
"Peach Bacterial Spot": "Apply copper sprays and remove infected parts.",
"Peach Healthy": "No treatment needed.",

# 🌶️ PEPPER
"Pepper Bell Bacterial Spot": "Use copper sprays and resistant varieties.",
"Pepper Bell Healthy": "No treatment needed.",

# 🍊 ORANGE
"Orange Haunglongbing Citrus Greening": "Control psyllids and remove infected trees.",

# 🍒 CHERRY
"Cherry Powdery Mildew": "Apply sulfur fungicides.",
"Cherry Healthy": "No treatment needed.",

# 🥬 CASSAVA
"Cassava Bacterial Blight Cbb": "Use disease-free cuttings and resistant varieties.",
"Cassava Brown Streak Disease Cbsd": "Remove infected plants and control vectors.",
"Cassava Green Mottle Cgm": "Use resistant varieties.",
"Cassava Mosaic Disease Cmd": "Control whiteflies and remove infected plants.",
"Cassava Healthy": "No treatment needed.",

# 🌾 RICE
"Rice Brownspot": "Apply balanced fertilizers and fungicides.",
"Rice Healthy": "No treatment needed.",
"Rice Hispa": "Use insecticides and remove infected leaves.",
"Rice Leafblast": "Apply fungicides like tricyclazole.",

# 🥒 SQUASH
"Squash Powdery Mildew": "Apply sulfur fungicides and ensure airflow.",

# 🫐 BLUEBERRY
"Blueberry Healthy": "No treatment needed.",

# 🌱 SOYBEAN
"Soybean Healthy": "No treatment needed.",

# 🍓 RASPBERRY
"Raspberry Healthy": "No treatment needed."

}


def get_treatment(disease):
    return treatments.get(
        disease,
        "General care: remove infected parts, improve hygiene, and use appropriate fungicides or pesticides."
    )