from fastapi import FastAPI
import gradio as gr
from app.interface import create_interface

app = FastAPI()
interface = create_interface(title="Parser")

# @app.get("/")
# async def root():
#     pass

gr.mount_gradio_app(app, interface, path="")