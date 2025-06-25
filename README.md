# 📊 Predicción de Ventas Semanales – Repostería

Este proyecto aplica Machine Learning para predecir la cantidad de unidades de productos de repostería vendidas semanalmente, basándose en variables como sabor, clima, promociones y actividad en redes sociales.

## 🧠 Tecnologías utilizadas

- Python
- Scikit-Learn (Regresión Lineal)
- Flask (API REST)
- Pandas, Joblib

## 📁 Estructura del proyecto

- `main.ipynb`: Entrenamiento y análisis del modelo
- `modelo_reposteria.pkl`: Modelo entrenado
- `app.py`: API Flask para realizar predicciones
- `demanda_reposteria.csv`: Dataset con +500 registros

## 🚀 Instrucciones para usar

1. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

2. Ejecutar la API:
   ```bash
   python app.py
   ```

## 📡 Endpoint `/predict` (POST)

**Ejemplo de entrada**:
```json
{
  "semana": 20,
  "sabor_producto": "vainilla",
  "clima": "soleado",
  "feriado": "no",
  "promocion": "sí",
  "redes_sociales": "sí"
}
```

**Respuesta esperada**:
```json
{
  "prediccion_unidades_vendidas": 34
}
```
