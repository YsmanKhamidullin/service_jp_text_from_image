# Translating text from screen to screen

[//]: # (### What and Why)

[//]: # ()

[//]: # (This project is for translating the text in your screen.)

### Getting start

Streamlit app:

```
git clone https://github.com/YsmanKhamidullin/ModelTraining.git
cd ModelTraining
python -m streamlit run app/api/streamlit_app.py
```

Open in browser: http://localhost:8501/

FastApi app:

```
git clone https://github.com/YsmanKhamidullin/ModelTraining.git
cd ModelTraining
python -m uvicorn app.api.fastapi_app:app 
```

Open in browser: http://127.0.0.1:8000/

### Current Implementation

* > Get jp text from image with [manga-ocr](https://github.com/kha-white/manga-ocr)
* > Using StreamLit and Fast Api for deploy
* > Testing ocr from git push (tests/test_fast_api.py)
* > Available online at: [StreamLit](https://ysmankhamidullin-modeltraining-appapistreamlit-app-bzphol.streamlit.app/)

### Misc info

- Developers
    - Maintainer: [Ysman Khamidullin](https://github.com/YsmanKhamidullin) RIM-130908
    - Contributors:
        - [Maksim Chechulin](https://github.com/YsmanKhamidullin) RIM-130908

# Model Source

[HuggingFace](https://huggingface.co/kha-white/manga-ocr-base), [GitHub](https://github.com/kha-white/manga-ocr)