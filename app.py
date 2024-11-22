import fastapi as FastAPI
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from textSummarizer.pipeline.prediction import PredictionPipeline

text: str = "What is Text Summarization?"

app = FastAPI.FastAPI()

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs") 


@app.get("/train")
async def train():
    try:
        os.system("python main.py")
        return Response(content="Training Completed", status_code=200)
    except Exception as e:
        return Response(f"Error Occured: {e}")
    

@app.post("/predict")
async def predict(text):
    try:
        obj = PredictionPipeline()
        text = obj.predict(text)
        return text
    except Exception as e:
        raise e
    

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)