from typing import Annotated
from fastapi import FastAPI, File
import app.modules.jp_ocr as jp_ocr

app = FastAPI()


@app.get("/")
async def root():
    test_answer = "Hello World"
    return {"message": test_answer}


@app.post("/ocr_image/")
async def ocr_image(file: Annotated[bytes, File()]):
    result = jp_ocr.extract_text_from_image(file)
    return {"text": result}
