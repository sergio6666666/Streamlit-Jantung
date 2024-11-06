import pickle
import numpy as np
import streamlit as st

# Load saved model
model = pickle.load(open('penyakit_jantung.sav', 'rb'))

# Judul web
st.title('Prediksi Penyakit Jantung')

col1, col2, col3 = st.columns(3)

# Input fields
with col1: 
    age = st.text_input('Umur')
with col2:
    sex = st.text_input('Jenis Kelamin')
with col3:
    cp = st.text_input('Jenis Nyeri Dada')
with col1:
    trestbps = st.text_input('Tekanan Darah')
with col2:
    chol = st.text_input('Nilai Kolesterol')
with col3:
    fbs = st.text_input('Gula Darah')
with col1:
    restecg = st.text_input('Hasil Elektrokardiografi')
with col2:
    thalach = st.text_input('Detak Jantung Maksimum')
with col3:
    exang = st.text_input('Induksi Angina')
with col1:
    oldpeak = st.text_input('ST Depression')
with col2:
    slope = st.text_input('Slope')
with col3:
    ca = st.text_input('Nilai CA')
with col2:
    thal = st.text_input('Nilai Thal')
    
# Kode untuk prediksii
heart_diagnosis = ''

# Membuat tombol prediksi
if st.button('Prediksi Penyakit Jantung'):
    try:
        # Convert inputs to float
        input_data = [
            float(age), float(sex), float(cp), float(trestbps),
            float(chol), float(fbs), float(restecg), float(thalach),
            float(exang), float(oldpeak), float(slope), float(ca), float(thal)
        ]
        
        # Prediction
        heart_prediction = model.predict([input_data])
        if heart_prediction[0] == 1:
            heart_diagnosis = 'Pasien Terkena Penyakit Jantung'
        else:
            heart_diagnosis = 'Pasien Tidak Terkena Penyakit Jantung'
        
    except ValueError:
        heart_diagnosis = 'Harap masukkan nilai numerik yang valid.'

st.success(heart_diagnosis)
