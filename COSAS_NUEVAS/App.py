# Importar Streamlit y otros módulos necesarios
import streamlit as st
import pandas as pd
#import joblib
import numpy as np

# Cargar el modelo entrenado con las 5 características más importantes
#rf_model_selected = joblib.load('random_forest_model_selected.pkl')

# Definir la aplicación Streamlit
def main():
    st.title('Aplicación de Predicción de Índice de Masa Corporal (IMC)')

    # Sidebar para la entrada de datos del usuario
    st.sidebar.header('Ingrese los datos del paciente:')

    # Recoger los datos del usuario
    edad = st.sidebar.number_input('Edad', min_value=18, max_value=100, step=1)
    peso = st.sidebar.number_input('Peso (kg)', min_value=30.0, max_value=300.0, step=0.1)
    altura = st.sidebar.number_input('Altura (cm)', min_value=100.0, max_value=250.0, step=0.1)
    nivel_actividad_fisica = st.sidebar.selectbox('Nivel de actividad física', ['Sedentario', 'Ligero', 'Moderado', 'Intenso'])
    consumo_alcohol = st.sidebar.selectbox('Consumo de alcohol', ['Bajo', 'Moderado', 'Alto'])

    # Predecir el IMC si se ingresan todos los datos
    if st.sidebar.button('Predecir IMC'):
        # Verificar si se han ingresado todos los datos necesarios
        if edad is not None and peso is not None and altura is not None and nivel_actividad_fisica is not None and consumo_alcohol is not None:
            # Convertir el nivel de actividad física en una codificación one-hot
            actividad_fisica_encoded = np.zeros(4)
            actividad_fisica_encoded[['Sedentario', 'Ligero', 'Moderado', 'Intenso'].index(nivel_actividad_fisica)] = 1

            # Convertir el consumo de alcohol en una codificación one-hot
            consumo_alcohol_encoded = np.zeros(3)
            consumo_alcohol_encoded[['Bajo', 'Moderado', 'Alto'].index(consumo_alcohol)] = 1
            
            # Preparar los datos para la predicción
            input_data = pd.DataFrame({
                'Edad': [edad],
                'Peso': [peso],
                'Altura': [altura],
                'Nivel_Actividad_Fisica_Sedentario': [actividad_fisica_encoded[0]],
                'Nivel_Actividad_Fisica_Ligero': [actividad_fisica_encoded[1]],
                'Nivel_Actividad_Fisica_Moderado': [actividad_fisica_encoded[2]],
                'Nivel_Actividad_Fisica_Intenso': [actividad_fisica_encoded[3]],
                'Consumo_Alcohol_Bajo': [consumo_alcohol_encoded[0]],
                'Consumo_Alcohol_Moderado': [consumo_alcohol_encoded[1]],
                'Consumo_Alcohol_Alto': [consumo_alcohol_encoded[2]]
            })

            # Realizar la predicción
            imc_pred = rf_model_selected.predict(input_data)

            # Mostrar el resultado de la predicción
            st.sidebar.success(f'El IMC predicho es: {imc_pred[0]:.2f}')
        else:
            # Mostrar un mensaje de error si no se han ingresado todos los datos necesarios
            st.sidebar.error('Por favor, complete todos los campos.')

# Ejecutar la aplicación
if __name__ == '__main__':
    main()
