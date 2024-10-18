import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image

# Set page configuration (must be the first Streamlit command)


# Load models for each plant
models = {
    "Potato": tf.keras.models.load_model('trained_plant_disease_model.h5'),
    #"Tomato": tf.keras.models.load_model(r'C:\Users\arman\Desktop\project roll no. 19\plantai\project_root\models\tomato1.h5'),
    "Rice": tf.keras.models.load_model('rice2.h5'),
    "Wheat": tf.keras.models.load_model('wheat1.h5'),
    "Apple": tf.keras.models.load_model('apple.h5'),
    "Corn": tf.keras.models.load_model('corn.h5'),
    "sugar_cane": tf.keras.models.load_model('sugarcane.h5')
}

# Define diseases and cures for each plant
plant_diseases = {
    "Potato": {
        "diseases": ["Potato___Early_blight", "Potato___Late_blight", "Potato___healthy"],
        "cures": [
            "Apply fungicide, remove infected leaves",
            "Prune infected branches, apply copper-based fungicides",
            "No treatment needed"
        ]
    },
    "Tomato": {
        "diseases": ['Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___healthy'],
        "cures": [
            "Apply fungicide, remove infected leaves",
            "Prune infected branches, apply copper-based fungicides",
            "No treatment needed",
             "Prune infected branches, apply copper-based fungicides",
              "Prune infected branches, apply copper-based fungicides",
               "Prune infected branches, apply copper-based fungicides",
                "Prune infected branches, apply copper-based fungicides",
                 "Prune infected branches, apply copper-based fungicides",
                 "Prune infected branches, apply copper-based fungicides",
                 "Prune infected branches, apply copper-based fungicides"                 
        ]
    },
    "Rice": {
        "diseases": ['Brownspot', 'Rice___Healthyt', 'Rice___Leaf_Blast', 'Rice___Neck_Blast', 'Tungro', 'bacterial blight'],
        "cures": [
            "Apply fungicide, remove infected leaves",
            "Prune infected branches, apply copper-based fungicides",
            "No treatment needed",
              "No treatment needed",
                "No treatment needed",
                  "No treatment needed"
        ]
    },
    "Wheat": {
        "diseases": ['Aphid', 'Black Rust', 'Blast', 'Brown Rust', 'Common Root Rot', 'Fusarium Head Blight', 'Healthy', 'Leaf Blight', ' powdery Mildew', 'Mite', 'Septoria', 'Smut', 'Stem fly', 'Tan spot', 'Yellow Rust'],
        "cures": [
            "Apply fungicide, remove infected leaves",
            "disease resistant varieties like H.P.W.- 360, 368, H.S.-562, H.S.-542 etc. After 2-3 years, replace them with new approved disease resistant 349, Grow varieties. As soon as the first symptoms of disease appear in the crop, spray Prapiconazole 25 EC. (0.1%) or Mancozeb 75 W.P. (0.2%) at an interval of 15 days.",
            "No treatment needed",
             "disease resistant varieties like H.P.W.- 360, 368, H.S.-562, H.S.-542 etc. After 2-3 years, replace them with new approved disease resistant 349, Grow varieties. As soon as the first symptoms of disease appear in the crop, spray Prapiconazole 25 EC. (0.1%) or Mancozeb 75 W.P. (0.2%) at an interval of 15 days.",
              "Prune infected branches, apply copper-based fungicides",
               "Prune infected branches, apply copper-based fungicides",
                "Prune infected branches, apply copper-based fungicides",
                 "Prune infected branches, apply copper-based fungicides",
                 "Spray Carbendazim (0.05%) on the crop at an interval of 15 days",
                 "Prune infected branches, apply copper-based fungicides",
                 "Prune infected branches, apply copper-based fungicides",
                 "Grow disease resistant varieties. Soak the seed for 6 hours in Propiconazole 25 solution E.C. and then go for sowing after drying the seed in shade or treat the seeds with Carbendazim (2.5 g/kg seed) or Rexil (1 g/kg seed). As soon as the symptoms of the disease appear, remove the diseased plants and burn them or bury them outside the field. Note: Treat seeds at the time of sowing.",
                 "Prune infected branches, apply copper-based fungicides",
                 "Prune infected branches, apply copper-based fungicides",
                 "disease resistant varieties like H.P.W.- 360, 368, H.S.-562, H.S.-542 etc. After 2-3 years, replace them with new approved disease resistant 349, Grow varieties. As soon as the first symptoms of disease appear in the crop, spray Prapiconazole 25 EC. (0.1%) or Mancozeb 75 W.P. (0.2%) at an interval of 15 days."                
        ]
    },
     "Apple": {
        "diseases": ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy', 'apple mosaic virus - Google Search', 'marssonina', 'powdery mildew apple - Google Search', 'scoty blotch and fly speach apple - Google Search'],
        "cures": [
            "Apply fungicide, remove infected leaves",
            "Prune infected branches, apply copper-based fungicides",
            "No treatment needed",
             "Prune infected branches, apply copper-based fungicides",
              "Prune infected branches, apply copper-based fungicides",
               "Prune infected branches, apply copper-based fungicides",
                "Prune infected branches, apply copper-based fungicides",
                 "Prune infected branches, apply copper-based fungicides"
                                
        ]
    },
      "Corn": {
        "diseases": ['Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 'Corn___Gray_Leaf_Spot', 'Corn___Phaeosphaeria_Leaf_Spot', 'Corn___Southern_Rust'],
        "cures": [
            "Apply fungicide, remove infected leaves",
            "Prune infected branches, apply copper-based fungicides",
            "No treatment needed",
             "Prune infected branches, apply copper-based fungicides",
              "Prune infected branches, apply copper-based fungicides",
               "Prune infected branches, apply copper-based fungicides",
                "Prune infected branches, apply copper-based fungicides"
                 
                                
        ]
    },
       "sugar_cane": {
        "diseases": ['Healthy', 'Mosaic', 'RedRot', 'Rust', 'SC Bacterial Bligh'],
        "cures": [
            "Apply fungicide, remove infected leaves",
            "Prune infected branches, apply copper-based fungicides",
            "No treatment needed",
            "Prune infected branches, apply copper-based fungicides",
            "No treatment needed"
        ]
    },
}

# Function to preprocess the uploaded image
def preprocess_image(image):
    img = image.resize((128, 128))  # Resize to the model input size
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Convert to a batch
    return img_array

# Function to predict disease and fetch cure
def detect_disease(image, plant):
    model = models[plant]
    predictions = model.predict(image)
    disease_index = np.argmax(predictions)
    print(disease_index)
    confidence = np.max(predictions) * 100
    
    disease = plant_diseases[plant]["diseases"][disease_index]
    cure = plant_diseases[plant]["cures"][disease_index]
    
    return disease, confidence, cure

#
