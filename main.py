from fastapi import FastAPI
import gradio as gr

app = FastAPI()

@app.get("/")
async def root():
    pass
    