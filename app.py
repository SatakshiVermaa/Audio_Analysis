from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import librosa
import soundfile as sf
import os
import uuid

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Audio API is up and running."}

@app.post("/predict-audio/")
async def predict_audio(file: UploadFile = File(...)):
    file_ext = os.path.splitext(file.filename)[1]
    if file_ext not in [".wav", ".mp3"]:
        return {"error": "Only .wav or .mp3 files are supported"}

    temp_filename = f"temp_{uuid.uuid4().hex}{file_ext}"
    with open(temp_filename, "wb") as buffer:
        buffer.write(await file.read())

    try:
        signal, sr = librosa.load(temp_filename, sr=None)
        duration = librosa.get_duration(y=signal, sr=sr)

        # Dummy prediction logic (replace with actual model)
        prediction = "speech detected" if duration > 1.0 else "too short"

        os.remove(temp_filename)

        return {
            "filename": file.filename,
            "duration": round(duration, 2),
            "prediction": prediction
        }

    except Exception as e:
        return {"error": str(e)}
