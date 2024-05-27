"""
FastAPI permet aussi bien de créer des API, que d'afficher une page @

Dans le terminal, saisir :
uvicorn main:app --reload
"""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
        <html>
            <head>
                <title>My FastAPI App</title>
            </head>
            <body>
                <h1>Hello, World!!!</h1>
            </body>
        </html>
    """

