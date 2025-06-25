# Aplicación de Predicción de Rendimiento Estudiantil

## Inicio 

1. Instalar dependencias:
```bash
pip install -r requirements.txt
```
2. Ejecutar el backend:
```bash
python backend/main.py
```
3. En otra terminal, ejecutar el frontend:
```bash
streamlit run frontend/app.py
```
4. Abrir en el navegador:
```bash
http://localhost:8501
```
## Estructura del proyecto:
proyecto/
├── backend/
│ ├── api/
│ │ ├── pycache/
│ │ └── main.py # Servidor principal de la API
│ ├── model/
│ │ └── modelo_entrenado.pkl # Modelo ML entrenado
│ └── student-mat.csv # Dataset original
├── frontend/
│ └── app.py # Aplicación Streamlit
├── notebooks/
│ └── train_model.ipynb # Notebook de entrenamiento
├── venv/ # Entorno virtual (opcional)
├── requirements.txt # Dependencias del proyecto
└── README.md # Documentación
