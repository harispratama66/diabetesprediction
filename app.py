import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("diabetes_model.pkl", "rb"))

# Judul aplikasi
st.title("Prediksi Diabetes")

# Input data dari user
pregnancies = st.number_input("Jumlah Kehamilan", min_value=0)
glucose = st.number_input("Glukosa", min_value=0)
blood_pressure = st.number_input("Tekanan Darah", min_value=0)
skin_thickness = st.number_input("Ketebalan Kulit", min_value=0)
insulin = st.number_input("Insulin", min_value=0)
bmi = st.number_input("BMI", min_value=0.0, format="%.2f")
diabetes_pedigree = st.number_input("Diabetes Pedigree Function", min_value=0.0, format="%.2f")
age = st.number_input("Usia", min_value=0)

# Tombol prediksi
if st.button("Prediksi"):
    # Buat array input
    input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]])
    
    # Prediksi
    prediction = model.predict(input_data)
    
    # Tampilkan hasil
    if prediction == 1:
        st.error("Hasil: Positif Diabetes")
    else:
        st.success("Hasil: Negatif Diabetes")
