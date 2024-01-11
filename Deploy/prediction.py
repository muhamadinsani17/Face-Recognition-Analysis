from PIL import Image
import requests
from io import BytesIO
import numpy as np
import streamlit as st
import tensorflow as tf
import io

# Memuat model dari direktori SavedModel
model_gender = tf.keras.models.load_model('model_gender')
model_ethnicity = tf.keras.models.load_model('model_ethnicity')
model_age = tf.keras.models.load_model('model_age')


# Mengubah ukuran gambar dan mengonversinya ke mode grayscale
def preprocess_image(img,):
    img = img.resize((48, 48))
    img_array = np.array(img.convert("L"))  # Convert ke mode grayscale
    img_array = img_array.reshape((*(48, 48), 1))  # Menambahkan dimensi kedalam
    img_array = img_array / 255.0  # Normalisasi
    input_image = np.expand_dims(img_array, axis=0)
    classes = model_gender.predict(input_image)
    classes1 = model_ethnicity.predict(input_image)
    classes2 = model_age.predict(input_image)
    idx = np.where(classes >= 0.32, 1, 0).item()
    idx1 = np.argmax(classes1, axis=1).item()
    idx2 = np.argmax(classes2, axis=1).item()
    label = ['Man','Woman']
    label1 = ['White', 'Black', 'Asian', 'Indian', 'Others']
    label2 = ['0-2','3-12', '13-18', '19-60', '60-116']
    return st.write(f'''
            Prediction Gender is a : {label[idx]} 

            Prediction Ethnicity is a : {label1[idx1]} 

            Prediction Age is a : {label2[idx2]}
            ''')

def run():
    st.image('https://biology.missouri.edu/sites/default/files/icons/2020-10/noun_community_2739772_1.png')
    st.markdown("<h1 style='text-align: center;'>Welcome to Gender, Ethnicity, and Age Prediction Models</h1>", unsafe_allow_html=True)
    st.markdown("========================================================================================")
    st.write('')       
        
    option = st.radio("Choose an option:", ["Upload Image", "Use Image URL"])

    if option == "Upload Image":
        # Unggah gambar dari widget Streamlit
        uploaded_file = st.file_uploader("Choose a file", type=["jpg", "jpeg", "png"])
        
        if uploaded_file is not None:
            img = Image.open(uploaded_file)
            preprocess_image(img)
            
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_column_width=True)
            

    elif option == "Use Image URL":
        
        # Masukkan URL gambar menggunakan widget input
        image_url = st.text_input("Enter the URL of the Image:")
        
        if st.button("Image Prediction"):
            if image_url:
                # Coba memuat dan memproses gambar dari URL
                try:
                    response = requests.get(image_url)
                    img = Image.open(BytesIO(response.content))
                    preprocess_image(img)
                    
                    image = Image.open(io.BytesIO(requests.get(image_url).content))
                    st.image(image, caption="Image from URL", use_column_width=True)

                except Exception as e:
                    st.error(f"Error: {e}")
            else:
                st.warning("Enter the image URL first.")


