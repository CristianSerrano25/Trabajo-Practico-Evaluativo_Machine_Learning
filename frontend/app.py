import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import os

st.set_page_config("Predicción de Abandono Escolar", layout="centered")
st.title("Dashboard de Predicción de Abandono Escolar")

# Sidebar
age = st.sidebar.slider("Edad", 15, 22, 17)
failures = st.sidebar.slider("Materias reprobadas", 0, 4, 1)
absences = st.sidebar.slider("Faltas", 0, 100, 5)
goout = st.sidebar.slider("Frecuencia de salidas", 1, 5, 3)
health = st.sidebar.slider("Salud", 1, 5, 3)
G1 = st.sidebar.slider("Nota G1", 0, 20, 10)
G2 = st.sidebar.slider("Nota G2", 0, 20, 10)

def cargar_historial():
    if os.path.exists("predicciones.csv"):
        return pd.read_csv("predicciones.csv", parse_dates=["timestamp"])
    return pd.DataFrame()

def guardar_prediccion(data):
    df_actual = pd.DataFrame([data])
    df_hist = cargar_historial()
    df_total = pd.concat([df_hist, df_actual], ignore_index=True)
    df_total.to_csv("predicciones.csv", index=False)

def mostrar_grafico_probabilidad(prob):
    fig, ax = plt.subplots()
    ax.bar(["Abandono", "Continua"], [prob, 1 - prob], color=["red", "green"])
    ax.set_ylim(0, 1)
    ax.set_ylabel("Probabilidad")
    st.pyplot(fig)

# Predicción
if st.sidebar.button("Predecir"):
    payload = {
        "age": age,
        "failures": failures,
        "absences": absences,
        "goout": goout,
        "health": health,
        "G1": G1,
        "G2": G2
    }
    try:
        response = requests.post("http://localhost:8000/predict", json=payload)
        result = response.json()
        prob = result["probabilidad"]
        st.subheader("Resultado de la predicción")
        if result["abandona"]:
            st.error(f"Riesgo ALTO de abandono (Prob: {prob})")
        else:
            st.success(f"Riesgo BAJO de abandono (Prob: {prob})")
        payload.update({
            "abandona": result["abandona"],
            "probabilidad": prob,
            "timestamp": datetime.now().isoformat()
        })
        guardar_prediccion(payload)
        st.subheader("📈 Probabilidad")
        mostrar_grafico_probabilidad(prob)
    except Exception as e:
        st.error(f"Error al conectar con la API: {e}")

# Historial
df_hist = cargar_historial()
if not df_hist.empty:
    st.divider()
    st.header("Análisis del historial de predicciones")
    st.metric("Total de predicciones", len(df_hist))
    st.metric("Abandono predicho (%)", f"{(df_hist['abandona'].mean()*100):.1f}%")
    st.subheader("Últimas predicciones")
    st.dataframe(df_hist.sort_values("timestamp", ascending=False).tail(10))
    st.subheader("Distribución de probabilidades")
    fig2, ax2 = plt.subplots()
    sns.histplot(df_hist["probabilidad"], bins=10, kde=True, ax=ax2, color="skyblue")
    st.pyplot(fig2)
