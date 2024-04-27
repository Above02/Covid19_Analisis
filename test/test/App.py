import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Verificar si el modelo ya está descargado
try:
    with open("rf_model.pkl", "rb") as f:
        rf_model = pickle.load(f)
except FileNotFoundError:
    # Si el archivo no está presente, descargarlo

# Implementar la aplicación Streamlit
st.title('Predicción de IMC')

# Sidebar
st.sidebar.header('Ingrese los datos del paciente')

# Definir las entradas del usuario
inputs = {}
inputs['Edad'] = st.sidebar.number_input('Edad', min_value=18, max_value=100, value=30)
inputs['Peso'] = st.sidebar.number_input('Peso (kg)', min_value=30.0, max_value=300.0, value=70.0)
inputs['Altura'] = st.sidebar.number_input('Altura (cm)', min_value=100.0, max_value=250.0, value=170.0)
inputs['Circunferencia de cintura'] = st.sidebar.number_input('Circunferencia de cintura (cm)', min_value=50.0, max_value=250.0, value=90.0)
inputs['Circunferencia de cadera'] = st.sidebar.number_input('Circunferencia de cadera (cm)', min_value=50.0, max_value=250.0, value=100.0)
inputs['Porcentaje de grasa corporal'] = st.sidebar.number_input('Porcentaje de grasa corporal (%)', min_value=5.0, max_value=50.0, value=25.0)
inputs['Historial médico familiar'] = st.sidebar.multiselect('Historial médico familiar', ['Diabetes', 'Hipertensión', 'Cáncer', 'Enfermedades cardiovasculares'])
inputs['Nivel de actividad física'] = st.sidebar.selectbox('Nivel de actividad física', ['Sedentario', 'Ligero', 'Moderado', 'Intenso'])
inputs['Hábitos alimenticios'] = st.sidebar.selectbox('Hábitos alimenticios', ['Vegetariano', 'Omnívoro', 'Vegano', 'Pescetariano', 'Keto', 'Paleo'])
inputs['Horas de sueño por noche'] = st.sidebar.number_input('Horas de sueño por noche', min_value=0, max_value=24, value=7)
inputs['Nivel de estrés percibido'] = st.sidebar.slider('Nivel de estrés percibido', min_value=1, max_value=10, value=5)
inputs['Consumo de agua diario'] = st.sidebar.number_input('Consumo de agua diario (litros)', min_value=0.0, max_value=5.0, value=2.0)
inputs['Consumo de alcohol'] = st.sidebar.number_input('Consumo de alcohol (unidades por semana)', min_value=0, max_value=20, value=5)
inputs['Consumo de tabaco'] = st.sidebar.number_input('Consumo de tabaco (cigarrillos por día)', min_value=0, max_value=20, value=5)
inputs['Consumo de cafeína'] = st.sidebar.number_input('Consumo de cafeína (mg por día)', min_value=0, max_value=500, value=200)
inputs['Enfermedades crónicas'] = st.sidebar.multiselect('Enfermedades crónicas', ['Diabetes', 'Hipertensión', 'Cáncer', 'Enfermedades cardiovasculares', 'Enfermedad renal crónica', 'Enfermedad pulmonar crónica'])
inputs['Medicamentos actuales'] = st.sidebar.multiselect('Medicamentos actuales', ['Aspirina', 'Insulina', 'Losartán', 'Atorvastatina', 'Metformina', 'Omeprazol', 'Salbutamol'])
inputs['Metas de pérdida de peso'] = st.sidebar.number_input('Metas de pérdida de peso (kg)', min_value=0.0, max_value=20.0, value=5.0)
inputs['Frecuencia cardíaca en reposo'] = st.sidebar.number_input('Frecuencia cardíaca en reposo (latidos por minuto)', min_value=40, max_value=120, value=70)
inputs['Presión arterial sistólica'] = st.sidebar.number_input('Presión arterial sistólica (mmHg)', min_value=80, max_value=200, value=120)
inputs['Presión arterial diastólica'] = st.sidebar.number_input('Presión arterial diastólica (mmHg)', min_value=40, max_value=120, value=80)
inputs['Nivel de colesterol (LDL)'] = st.sidebar.number_input('Nivel de colesterol (LDL) (mg/dL)', min_value=50, max_value=250, value=100)
inputs['Nivel de colesterol (HDL)'] = st.sidebar.number_input('Nivel de colesterol (HDL) (mg/dL)', min_value=20, max_value=100, value=50)
inputs['Nivel de colesterol (Triglicéridos)'] = st.sidebar.number_input('Nivel de colesterol (Triglicéridos) (mg/dL)', min_value=50, max_value=400, value=150)
inputs['Nivel de glucosa en sangre (Ayunas)'] = st.sidebar.number_input('Nivel de glucosa en sangre (Ayunas) (mg/dL)', min_value=50, max_value=200, value=90)
inputs['Nivel de glucosa en sangre (Postprandial)'] = st.sidebar.number_input('Nivel de glucosa en sangre (Postprandial) (mg/dL)', min_value=50, max_value=250, value=120)
inputs['Sensibilidad a ciertos alimentos'] = st.sidebar.multiselect('Sensibilidad a ciertos alimentos', ['Lactosa', 'Gluten', 'Nueces', 'Mariscos', 'Huevo', 'Soja'])
inputs['Nivel de satisfacción con la dieta actual'] = st.sidebar.slider('Nivel de satisfacción con la dieta actual', min_value=1, max_value=10, value=5)
inputs['Cumplimiento con el plan nutricional'] = st.sidebar.slider('Cumplimiento con el plan nutricional', min_value=1, max_value=10, value=5)
inputs['Actividades físicas realizadas'] = st.sidebar.multiselect('Actividades físicas realizadas', ['Caminar', 'Correr', 'Nadar', 'Bailar', 'Levantamiento de pesas', 'Yoga'])
inputs['Consumo de frutas y verduras'] = st.sidebar.number_input('Consumo de frutas y verduras (porciones por día)', min_value=0, max_value=10, value=5)
inputs['Nivel de conocimiento sobre nutrición'] = st.sidebar.selectbox('Nivel de conocimiento sobre nutrición', ['Bajo', 'Medio', 'Alto'])

# Realizar la predicción
input_df = pd.DataFrame([inputs])
prediction = rf_model.predict(input_df)

# Mostrar la predicción
st.subheader('Resultado')
st.write(f'El IMC predicho es: {prediction[0]}')

# Información adicional
st.subheader('Información Adicional')
st.write('Este modelo fue entrenado utilizando un conjunto de datos simulados de pacientes con características relacionadas con la salud y el estilo de vida. Utiliza un modelo de Random Forest Regresor para predecir el Índice de Masa Corporal (IMC) de un paciente.')
