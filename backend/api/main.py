from fastapi import FastAPI
import pickle
import numpy as np
from pydantic import BaseModel

app = FastAPI()

# Modelo
with open("../model/modelo_entrenado.pkl", "rb") as f:
    model = pickle.load(f)

class Estudiante(BaseModel):
    age: int
    failures: int
    absences: int
    goout: int
    health: int
    G1: int
    G2: int

@app.post("/predict")
def predecir(est: Estudiante):
    datos = np.array([[est.age, est.failures, est.absences, est.goout, est.health, est.G1, est.G2]])
    pred = model.predict(datos)[0]
    prob = model.predict_proba(datos)[0][1]
    return {"abandona": int(pred), "probabilidad": round(prob, 2)}
